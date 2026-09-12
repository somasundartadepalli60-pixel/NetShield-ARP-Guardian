# Humanization note: Keep incident state transitions explicit so an alert cannot disappear simply because a view changed. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
import json
from datetime import datetime, timezone

class IncidentService:
    def __init__(self, db):
        self.db=db

    def create_from_alert(self, alert):
        now=datetime.now(timezone.utc).isoformat()
        title=f"ARP security incident — {alert['source_ip']}"
        timeline=[{"time":now,"type":"alert","message":alert["message"],"risk":alert["risk_score"]}]
        recommendations=[
            "Validate the expected gateway/device MAC using an authorized trusted source.",
            "Review recent ARP mapping changes for the affected IP.",
            "Investigate the endpoint before taking disruptive containment action."
        ]
        with self.db.connect() as db:
            cur=db.execute("""INSERT INTO incidents(title,description,severity,status,created_at,updated_at,affected_ip,affected_mac,timeline,recommendations)
                              VALUES(?,?,?,?,?,?,?,?,?,?)""",
                (title,alert["message"],alert["severity"],"open",now,now,alert["source_ip"],alert["observed_mac"],
                 json.dumps(timeline),json.dumps(recommendations)))
            incident_id=cur.lastrowid
            db.execute("UPDATE alerts SET incident_id=? WHERE id=?",(incident_id,alert["id"]))
            return self.get(incident_id)

    def get(self, incident_id):
        with self.db.connect() as db:
            row=db.execute("SELECT * FROM incidents WHERE id=?",(incident_id,)).fetchone()
            return dict(row) if row else None

    def list(self):
        with self.db.connect() as db:
            return [dict(r) for r in db.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()]
