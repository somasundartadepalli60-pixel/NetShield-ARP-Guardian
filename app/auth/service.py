"""Local security authentication for the NetShield console.

Uses only Python standard-library cryptography primitives:
PBKDF2-HMAC-SHA256 password hashing, random session tokens, signed-by-storage
session lookup, CSRF tokens, expiration, and in-memory login throttling.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import secrets
import time
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Any

PBKDF2_ROUNDS = int(os.getenv("NETSHIELD_PBKDF2_ROUNDS", "240000"))
SESSION_MINUTES = int(os.getenv("NETSHIELD_SESSION_MINUTES", "30"))
MAX_FAILURES = int(os.getenv("NETSHIELD_MAX_LOGIN_FAILURES", "5"))
LOCK_MINUTES = int(os.getenv("NETSHIELD_LOCK_MINUTES", "15"))
COOKIE_NAME = "netshield_session"
CSRF_HEADER = "X-CSRF-Token"

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def iso_now() -> str:
    return utc_now().isoformat()

def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    if not isinstance(password, str) or len(password) < 12:
        raise ValueError("Password must contain at least 12 characters")
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ROUNDS
    )
    return salt.hex(), digest.hex()

def verify_password(password: str, salt_hex: str, digest_hex: str) -> bool:
    try:
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
    except ValueError:
        return False
    actual = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ROUNDS
    )
    return hmac.compare_digest(actual, expected)

def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()

@dataclass(slots=True)
class AuthUser:
    id: int
    username: str
    role: str
    display_name: str
    must_change_password: bool = False

class AuthService:
    """Database-backed sessions with local password authentication."""

    def __init__(self, db):
        self.db = db
        self._failures: dict[str, list[float]] = {}

    def initialize(self) -> None:
        with self.db.connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS auth_users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_salt TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'admin',
                display_name TEXT NOT NULL,
                failed_attempts INTEGER NOT NULL DEFAULT 0,
                locked_until TEXT,
                must_change_password INTEGER NOT NULL DEFAULT 1,
                password_changed_at TEXT,
                created_at TEXT NOT NULL,
                last_login_at TEXT
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS auth_sessions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token_hash TEXT NOT NULL UNIQUE,
                csrf_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                last_seen_at TEXT NOT NULL,
                user_agent TEXT,
                FOREIGN KEY(user_id) REFERENCES auth_users(id) ON DELETE CASCADE
            )""")
            db.execute("CREATE INDEX IF NOT EXISTS idx_auth_sessions_token ON auth_sessions(token_hash)")
            db.execute("CREATE INDEX IF NOT EXISTS idx_auth_sessions_expiry ON auth_sessions(expires_at)")
            row = db.execute("SELECT id FROM auth_users LIMIT 1").fetchone()
            if not row:
                # Local-first bootstrap. Override before production use.
                password = os.getenv("NETSHIELD_ADMIN_PASSWORD", "ChangeMe-NetShield-2026!")
                salt, digest = hash_password(password)
                db.execute("""INSERT INTO auth_users
                    (username,password_salt,password_hash,role,display_name,
                     must_change_password,created_at)
                    VALUES(?,?,?,?,?,?,?)""",
                    ("admin", salt, digest, "security-admin", "Security Administrator", 1, iso_now()))

    def _locked(self, row: Any) -> bool:
        value = row["locked_until"]
        if not value:
            return False
        try:
            return datetime.fromisoformat(value) > utc_now()
        except ValueError:
            return False

    def _rate_limited(self, username: str) -> bool:
        now = time.time()
        recent = [x for x in self._failures.get(username.lower(), []) if now - x < 900]
        self._failures[username.lower()] = recent
        return len(recent) >= MAX_FAILURES

    def authenticate(self, username: str, password: str) -> AuthUser:
        username = username.strip().lower()
        if not username or not password:
            raise ValueError("Username and password are required")
        if self._rate_limited(username):
            raise PermissionError("Too many failed attempts; try again later")
        with self.db.connect() as db:
            row = db.execute("SELECT * FROM auth_users WHERE username=?", (username,)).fetchone()
            if not row or self._locked(row) or not verify_password(
                password, row["password_salt"], row["password_hash"]
            ):
                self._failures.setdefault(username, []).append(time.time())
                if row:
                    failed = int(row["failed_attempts"]) + 1
                    lock = None
                    if failed >= MAX_FAILURES:
                        lock = (utc_now() + timedelta(minutes=LOCK_MINUTES)).isoformat()
                    db.execute("UPDATE auth_users SET failed_attempts=?,locked_until=? WHERE id=?",
                               (failed, lock, row["id"]))
                raise PermissionError("Invalid credentials")
            db.execute("""UPDATE auth_users
                SET failed_attempts=0,locked_until=NULL,last_login_at=?
                WHERE id=?""", (iso_now(), row["id"]))
            self._failures.pop(username, None)
            return AuthUser(row["id"], row["username"], row["role"], row["display_name"],
                            bool(row["must_change_password"]))

    def create_session(self, user: AuthUser, user_agent: str = "") -> tuple[str, str, datetime]:
        token = secrets.token_urlsafe(48)
        csrf = secrets.token_urlsafe(32)
        created = utc_now()
        expires = created + timedelta(minutes=SESSION_MINUTES)
        with self.db.connect() as db:
            db.execute("""INSERT INTO auth_sessions
                (user_id,token_hash,csrf_hash,created_at,expires_at,last_seen_at,user_agent)
                VALUES(?,?,?,?,?,?,?)""",
                (user.id, token_hash(token), token_hash(csrf), created.isoformat(),
                 expires.isoformat(), created.isoformat(), user_agent[:300]))
        return token, csrf, expires

    def current_user(self, token: str | None) -> tuple[AuthUser, str] | None:
        if not token:
            return None
        with self.db.connect() as db:
            row = db.execute("""SELECT u.*,s.csrf_hash,s.expires_at
                FROM auth_sessions s JOIN auth_users u ON u.id=s.user_id
                WHERE s.token_hash=?""", (token_hash(token),)).fetchone()
            if not row:
                return None
            try:
                expires = datetime.fromisoformat(row["expires_at"])
            except ValueError:
                return None
            if expires <= utc_now():
                db.execute("DELETE FROM auth_sessions WHERE id=?", (row["id"],))
                return None
            db.execute("UPDATE auth_sessions SET last_seen_at=? WHERE id=?",
                       (iso_now(), row["id"]))
            return AuthUser(row["id"], row["username"], row["role"], row["display_name"],
                            bool(row["must_change_password"])), row["csrf_hash"]

    def valid_csrf(self, csrf: str | None, csrf_hash: str) -> bool:
        return bool(csrf) and hmac.compare_digest(token_hash(csrf), csrf_hash)

    def create_csrf_token(self, token: str | None) -> str | None:
        if not token or not self.current_user(token):
            return None
        csrf = secrets.token_urlsafe(32)
        with self.db.connect() as db:
            db.execute("UPDATE auth_sessions SET csrf_hash=? WHERE token_hash=?",
                       (token_hash(csrf), token_hash(token)))
        return csrf

    def logout(self, token: str | None) -> None:
        if token:
            with self.db.connect() as db:
                db.execute("DELETE FROM auth_sessions WHERE token_hash=?", (token_hash(token),))

    def change_password(self, user_id: int, old_password: str, new_password: str) -> None:
        if len(new_password) < 12:
            raise ValueError("New password must contain at least 12 characters")
        with self.db.connect() as db:
            row = db.execute("SELECT * FROM auth_users WHERE id=?", (user_id,)).fetchone()
            if not row or not verify_password(old_password, row["password_salt"], row["password_hash"]):
                raise PermissionError("Current password is incorrect")
            salt, digest = hash_password(new_password)
            db.execute("""UPDATE auth_users SET password_salt=?,password_hash=?,
                must_change_password=0,password_changed_at=? WHERE id=?""",
                       (salt, digest, iso_now(), user_id))
