# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The __init__ entry point keeps that boundary visible to readers.
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


class Database:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()

    def initialize(self) -> None:
        with self.connect() as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY, ip_address TEXT UNIQUE NOT NULL,
                mac_address TEXT NOT NULL, hostname TEXT, status TEXT NOT NULL DEFAULT 'normal',
                trusted INTEGER NOT NULL DEFAULT 0, first_seen TEXT NOT NULL, last_seen TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS arp_events (
                id INTEGER PRIMARY KEY, source_ip TEXT NOT NULL, source_mac TEXT NOT NULL,
                target_ip TEXT NOT NULL, target_mac TEXT NOT NULL, operation TEXT NOT NULL,
                timestamp TEXT NOT NULL, interface TEXT NOT NULL, risk_score INTEGER NOT NULL DEFAULT 0,
                detection_result TEXT NOT NULL DEFAULT 'normal'
            );
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY, alert_type TEXT NOT NULL, severity TEXT NOT NULL,
                source_ip TEXT NOT NULL, expected_mac TEXT, observed_mac TEXT NOT NULL,
                message TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'open',
                created_at TEXT NOT NULL, acknowledged_at TEXT, risk_score INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS detection_rules (
                id INTEGER PRIMARY KEY, rule_id TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
                description TEXT NOT NULL, severity TEXT NOT NULL, enabled INTEGER NOT NULL DEFAULT 1,
                threshold INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY, key TEXT UNIQUE NOT NULL, value TEXT NOT NULL, updated_at TEXT NOT NULL
            );
            """)
            rules = [
                ("ARP-001", "Unexpected MAC change", "An IP address is announced by a new MAC.", "medium", 30),
                ("ARP-002", "Gateway MAC change", "The configured gateway identity changes.", "high", 60),
                ("ARP-003", "Duplicate IP ownership", "Multiple devices claim the same IP address.", "high", 60),
                ("ARP-004", "Rapid MAC reassignment", "Repeated identity changes occur in a short period.", "high", 50),
                ("ARP-005", "Unsolicited ARP reply", "A reply was received without a matching request context.", "low", 20),
            ]
            db.executemany("INSERT OR IGNORE INTO detection_rules(rule_id,name,description,severity,threshold) VALUES (?,?,?,?,?)", rules)
            db.execute("INSERT OR IGNORE INTO settings(key,value,updated_at) VALUES ('gateway_ip','192.168.1.1',datetime('now'))")
            db.execute("INSERT OR IGNORE INTO settings(key,value,updated_at) VALUES ('risk_threshold','30',datetime('now'))")
