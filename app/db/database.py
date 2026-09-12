# Humanization note: Keep database access explicit because security state should be easy to inspect during an incident. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS devices(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 ip_address TEXT NOT NULL UNIQUE,
 mac_address TEXT NOT NULL,
 hostname TEXT,
 status TEXT NOT NULL DEFAULT 'unknown',
 trusted INTEGER NOT NULL DEFAULT 0,
 first_seen TEXT NOT NULL,
 last_seen TEXT NOT NULL,
 risk_score INTEGER NOT NULL DEFAULT 0,
 interface TEXT NOT NULL DEFAULT 'unknown'
);
CREATE TABLE IF NOT EXISTS arp_events(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 source_ip TEXT NOT NULL,
 source_mac TEXT NOT NULL,
 target_ip TEXT NOT NULL,
 target_mac TEXT NOT NULL,
 operation TEXT NOT NULL,
 timestamp TEXT NOT NULL,
 interface TEXT NOT NULL,
 risk_score INTEGER NOT NULL DEFAULT 0,
 confidence REAL NOT NULL DEFAULT 0,
 severity TEXT NOT NULL DEFAULT 'info',
 detection_result TEXT NOT NULL DEFAULT 'normal',
 reasons TEXT NOT NULL DEFAULT '',
 detector_ids TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_arp_events_source_ip ON arp_events(source_ip);
CREATE INDEX IF NOT EXISTS idx_arp_events_timestamp ON arp_events(timestamp);
CREATE INDEX IF NOT EXISTS idx_arp_events_risk ON arp_events(risk_score);

CREATE TABLE IF NOT EXISTS alerts(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 alert_type TEXT NOT NULL,
 severity TEXT NOT NULL,
 source_ip TEXT NOT NULL,
 expected_mac TEXT,
 observed_mac TEXT NOT NULL,
 message TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'new',
 created_at TEXT NOT NULL,
 acknowledged_at TEXT,
 resolved_at TEXT,
 risk_score INTEGER NOT NULL,
 confidence REAL NOT NULL DEFAULT 0,
 incident_id INTEGER
);
CREATE INDEX IF NOT EXISTS idx_alerts_status ON alerts(status);
CREATE INDEX IF NOT EXISTS idx_alerts_created ON alerts(created_at);

CREATE TABLE IF NOT EXISTS detection_rules(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 rule_id TEXT UNIQUE NOT NULL,
 name TEXT NOT NULL,
 description TEXT NOT NULL,
 severity TEXT NOT NULL,
 enabled INTEGER NOT NULL DEFAULT 1,
 threshold INTEGER NOT NULL,
 window_seconds INTEGER NOT NULL DEFAULT 60
);

CREATE TABLE IF NOT EXISTS baselines(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 network_key TEXT NOT NULL,
 ip_address TEXT NOT NULL,
 mac_address TEXT NOT NULL,
 observations INTEGER NOT NULL DEFAULT 0,
 confidence REAL NOT NULL DEFAULT 0,
 first_seen TEXT NOT NULL,
 last_seen TEXT NOT NULL,
 UNIQUE(network_key, ip_address, mac_address)
);

CREATE TABLE IF NOT EXISTS incidents(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 description TEXT NOT NULL,
 severity TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'open',
 created_at TEXT NOT NULL,
 updated_at TEXT NOT NULL,
 affected_ip TEXT,
 affected_mac TEXT,
 timeline TEXT NOT NULL DEFAULT '[]',
 recommendations TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS audit_logs(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 actor TEXT NOT NULL,
 action TEXT NOT NULL,
 resource_type TEXT NOT NULL,
 resource_id TEXT,
 details TEXT NOT NULL DEFAULT '{}',
 created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS settings(
 key TEXT PRIMARY KEY,
 value TEXT NOT NULL,
 updated_at TEXT NOT NULL
);
"""

DEFAULT_RULES = [
 ("ARP-001","Unexpected MAC change","Known IP suddenly appears with a different MAC.","medium",35,60),
 ("ARP-002","Gateway identity change","The monitored gateway IP changes MAC identity.","critical",65,60),
 ("ARP-003","Duplicate IP ownership","One IP is observed from multiple MAC identities.","high",55,120),
 ("ARP-004","Rapid reassignment","Repeated IP/MAC identity changes occur in a short window.","high",50,60),
 ("ARP-005","Unsolicited reply","A reply appears without a known request context.","low",20,30),
 ("ARP-006","ARP burst","ARP activity exceeds the configured rate baseline.","medium",40,30),
 ("ARP-007","Gratuitous conflict","Gratuitous ARP conflicts with the learned identity.","high",60,60),
]

class Database:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        db = sqlite3.connect(self.path, timeout=15)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def initialize(self) -> None:
        with self.connect() as db:
            db.executescript(SCHEMA)
            db.executemany(
                """INSERT OR IGNORE INTO detection_rules
                   (rule_id,name,description,severity,threshold,window_seconds)
                   VALUES (?,?,?,?,?,?)""", DEFAULT_RULES)
            db.execute("INSERT OR IGNORE INTO settings(key,value,updated_at) VALUES('gateway_ip','192.168.1.1',datetime('now'))")
            db.execute("INSERT OR IGNORE INTO settings(key,value,updated_at) VALUES('risk_threshold','35',datetime('now'))")
            db.execute("INSERT OR IGNORE INTO settings(key,value,updated_at) VALUES('monitoring_enabled','1',datetime('now'))")

    def setting(self, key: str, default: str) -> str:
        with self.connect() as db:
            row = db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
            return row["value"] if row else default
