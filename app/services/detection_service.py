from __future__ import annotations
import json
from datetime import datetime, timezone
from app.core.types import ArpObservation, Operation
from app.core.validation import normalize_mac, validate_ip
from app.core.types import DetectionSignal
from app.detection.detectors import DEFAULT_DETECTORS, DetectionContext
from app.scoring.engine import RiskScorer

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

class DetectionService:
    def __init__(self, db, manager):
        self.db = db
        self.manager = manager
        self.scorer = RiskScorer()

    def _rows(self, db, sql, params=()):
        return [dict(r) for r in db.execute(sql, params).fetchall()]

    async def evaluate(self, payload) -> dict:
        obs = ArpObservation(
            source_ip=validate_ip(payload.source_ip),
            source_mac=normalize_mac(payload.source_mac),
            target_ip=validate_ip(payload.target_ip),
            target_mac=normalize_mac(payload.target_mac),
            operation=Operation(payload.operation),
            interface=payload.interface,
            packet_length=payload.packet_length,
            is_broadcast=payload.is_broadcast,
            is_gratuitous=payload.is_gratuitous,
        )
        timestamp = now_iso()
        with self.db.connect() as db:
            device = db.execute("SELECT * FROM devices WHERE ip_address=?", (obs.source_ip,)).fetchone()
            known_mac = device["mac_address"] if device else None
            trusted = bool(device["trusted"]) if device else False
            gateway_ip = self._setting(db, "gateway_ip", "192.168.1.1")
            gateway = db.execute("SELECT mac_address FROM devices WHERE ip_address=?", (gateway_ip,)).fetchone()
            gateway_mac = gateway["mac_address"] if gateway else None
            recent = self._rows(db, """SELECT source_ip,source_mac,target_ip,target_mac,operation,timestamp
                                      FROM arp_events WHERE source_ip=? ORDER BY id DESC LIMIT 50""",(obs.source_ip,))
            recent_macs = [r["source_mac"] for r in recent]
            request_seen = any(r["operation"]=="request" and r["target_ip"]==obs.target_ip for r in recent)
            baseline = db.execute("""SELECT confidence FROM baselines
                                     WHERE ip_address=? AND mac_address=?
                                     ORDER BY last_seen DESC LIMIT 1""",(obs.source_ip,obs.source_mac)).fetchone()
            ctx = DetectionContext(known_mac,trusted,gateway_ip,gateway_mac,recent_macs,recent,float(baseline["confidence"]) if baseline else 0.0,request_seen)
            signals = [s for detector in DEFAULT_DETECTORS if (s:=detector.evaluate(obs,ctx))]
            decision = self.scorer.score(signals,trusted)
            # Keep the baseline independent from the alert decision so the first observation can establish context.
            from app.baselines.service import BaselineService
            BaselineService(self.db).observe("local", obs.source_ip, obs.source_mac)
            reasons = "; ".join(decision.reasons)
            detector_ids = ",".join(s.detector_id for s in signals)
            cur = db.execute("""INSERT INTO arp_events
                (source_ip,source_mac,target_ip,target_mac,operation,timestamp,interface,risk_score,confidence,severity,detection_result,reasons,detector_ids)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (obs.source_ip,obs.source_mac,obs.target_ip,obs.target_mac,obs.operation.value,timestamp,obs.interface,
                 decision.risk_score,decision.confidence,decision.severity.value,decision.result,reasons,detector_ids))
            event_id = cur.lastrowid
            if device:
                new_status = "suspicious" if decision.result=="suspicious" else ("trusted" if trusted else device["status"])
                db.execute("""UPDATE devices SET mac_address=?,last_seen=?,status=?,risk_score=?,interface=?
                              WHERE id=?""",(obs.source_mac,timestamp,new_status,decision.risk_score,obs.interface,device["id"]))
            else:
                db.execute("""INSERT INTO devices(ip_address,mac_address,status,trusted,first_seen,last_seen,risk_score,interface)
                              VALUES (?,?,?,?,?,?,?,?)""",
                           (obs.source_ip,obs.source_mac,"suspicious" if decision.result=="suspicious" else "unknown",0,timestamp,timestamp,decision.risk_score,obs.interface))
            alert = None
            threshold = int(self._setting(db,"risk_threshold","35"))
            if decision.risk_score >= threshold:
                cur = db.execute("""INSERT INTO alerts(alert_type,severity,source_ip,expected_mac,observed_mac,message,created_at,risk_score,confidence)
                                    VALUES (?,?,?,?,?,?,?,?,?)""",
                    ("ARP anomaly",decision.severity.value,obs.source_ip,known_mac,obs.source_mac,
                     reasons or "ARP activity exceeded the configured risk threshold.",timestamp,decision.risk_score,decision.confidence))
                alert = {"id":cur.lastrowid,"alert_type":"ARP anomaly","severity":decision.severity.value,
                         "source_ip":obs.source_ip,"expected_mac":known_mac,"observed_mac":obs.source_mac,
                         "message":reasons or "ARP activity exceeded the configured risk threshold.",
                         "status":"new","created_at":timestamp,"risk_score":decision.risk_score,"confidence":decision.confidence}
            event = {"id":event_id,"source_ip":obs.source_ip,"source_mac":obs.source_mac,"target_ip":obs.target_ip,
                     "target_mac":obs.target_mac,"operation":obs.operation.value,"timestamp":timestamp,
                     "interface":obs.interface,"risk_score":decision.risk_score,"confidence":decision.confidence,
                     "severity":decision.severity.value,"detection_result":decision.result,"reasons":decision.reasons,
                     "detector_ids":[s.detector_id for s in signals],"recommendation":decision.recommendation,"alert":alert}
        await self.manager.broadcast({"type":"arp_event","event":event})
        if alert:
            await self.manager.broadcast({"type":"alert","alert":alert})
        return event

    @staticmethod
    def _setting(db,key,fallback):
        row=db.execute("SELECT value FROM settings WHERE key=?",(key,)).fetchone()
        return row["value"] if row else fallback
