# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The utc_now entry point keeps that boundary visible to readers.
from datetime import datetime, timezone
import re
from .database import Database
from .realtime import ConnectionManager
from .schemas import ObservationIn


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_mac(value: str) -> str:
    compact = re.sub(r"[^0-9a-fA-F]", "", value).lower()
    if len(compact) != 12:
        raise ValueError("MAC address must contain 12 hexadecimal characters")
    return ":".join(compact[index:index + 2] for index in range(0, 12, 2))


class DetectionEngine:
    def __init__(self, database: Database, manager: ConnectionManager):
        self.database = database
        self.manager = manager

    async def evaluate(self, observation: ObservationIn) -> dict:
        source_mac = normalize_mac(observation.source_mac)
        target_mac = normalize_mac(observation.target_mac)
        timestamp = utc_now()
        risk = 0
        reasons: list[str] = []
        with self.database.connect() as db:
            device = db.execute("SELECT * FROM devices WHERE ip_address = ?", (observation.source_ip,)).fetchone()
            expected_mac = device["mac_address"] if device else None
            trusted = bool(device["trusted"]) if device else False
            if device and expected_mac != source_mac:
                risk += 30
                reasons.append("Unexpected MAC change")
                if observation.source_ip == self._setting(db, "gateway_ip", "192.168.1.1"):
                    risk += 40
                    reasons.append("Gateway impersonation")
                if trusted:
                    risk = max(0, risk - 20)
                    reasons.append("Trusted device adjustment")
            elif not device:
                expected_mac = None
            if observation.operation == "reply" and target_mac == "00:00:00:00:00:00":
                risk += 20
                reasons.append("Suspicious ARP reply")
            risk = min(100, risk)
            result = "suspicious" if risk >= 30 else "normal"
            severity = self._severity(risk)
            event_cursor = db.execute("""INSERT INTO arp_events(source_ip,source_mac,target_ip,target_mac,operation,timestamp,interface,risk_score,detection_result)
                                      VALUES (?,?,?,?,?,?,?,?,?)""", (observation.source_ip, source_mac, observation.target_ip, target_mac, observation.operation, timestamp, observation.interface, risk, result))
            if device:
                status = "suspicious" if result == "suspicious" else device["status"]
                db.execute("UPDATE devices SET mac_address=?,last_seen=?,status=? WHERE ip_address=?", (source_mac, timestamp, status, observation.source_ip))
            else:
                db.execute("""INSERT INTO devices(ip_address,mac_address,status,trusted,first_seen,last_seen) VALUES (?,?,?,0,?,?)""", (observation.source_ip, source_mac, "suspicious" if result == "suspicious" else "normal", timestamp, timestamp))
            alert = None
            if risk >= int(self._setting(db, "risk_threshold", "30")):
                message = "; ".join(reasons) or "ARP activity exceeded the configured risk threshold"
                cursor = db.execute("""INSERT INTO alerts(alert_type,severity,source_ip,expected_mac,observed_mac,message,created_at,risk_score)
                                    VALUES (?,?,?,?,?,?,?,?)""", ("ARP spoofing suspected", severity, observation.source_ip, expected_mac, source_mac, message, timestamp, risk))
                alert = {"id": cursor.lastrowid, "alert_type": "ARP spoofing suspected", "severity": severity, "source_ip": observation.source_ip, "expected_mac": expected_mac, "observed_mac": source_mac, "message": message, "status": "open", "created_at": timestamp, "risk_score": risk}
            event = {"id": event_cursor.lastrowid, "source_ip": observation.source_ip, "source_mac": source_mac, "target_ip": observation.target_ip, "target_mac": target_mac, "operation": observation.operation, "timestamp": timestamp, "interface": observation.interface, "risk_score": risk, "detection_result": result, "alert": alert}
        await self.manager.broadcast({"type": "arp_event", "event": event})
        if alert:
            await self.manager.broadcast({"type": "alert", "alert": alert})
        return event

    @staticmethod
    def _setting(db, key: str, fallback: str) -> str:
        row = db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        return row["value"] if row else fallback

    @staticmethod
    def _severity(risk: int) -> str:
        if risk >= 80:
            return "critical"
        if risk >= 60:
            return "high"
        if risk >= 30:
            return "medium"
        return "low"
