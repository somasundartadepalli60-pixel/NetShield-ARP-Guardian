# Humanization note: Keep exports deterministic so generated evidence can be compared in tests and reviews. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
import csv, io, json
from datetime import datetime, timezone

class ReportService:
    def __init__(self, db):
        self.db=db

    def summary(self):
        with self.db.connect() as db:
            return {
                "generated_at":datetime.now(timezone.utc).isoformat(),
                "devices":db.execute("SELECT COUNT(*) FROM devices").fetchone()[0],
                "events":db.execute("SELECT COUNT(*) FROM arp_events").fetchone()[0],
                "alerts":db.execute("SELECT COUNT(*) FROM alerts").fetchone()[0],
                "open_alerts":db.execute("SELECT COUNT(*) FROM alerts WHERE status NOT IN ('resolved','closed','false_positive')").fetchone()[0],
                "critical_alerts":db.execute("SELECT COUNT(*) FROM alerts WHERE severity='critical'").fetchone()[0],
                "high_alerts":db.execute("SELECT COUNT(*) FROM alerts WHERE severity='high'").fetchone()[0],
                "suspicious_events":db.execute("SELECT COUNT(*) FROM arp_events WHERE detection_result='suspicious'").fetchone()[0],
            }

    def events_csv(self):
        with self.db.connect() as db:
            rows=[dict(r) for r in db.execute("SELECT * FROM arp_events ORDER BY id DESC LIMIT 5000").fetchall()]
        out=io.StringIO()
        fields=list(rows[0].keys()) if rows else ["id","source_ip","source_mac","risk_score"]
        writer=csv.DictWriter(out,fieldnames=fields); writer.writeheader(); writer.writerows(rows)
        return out.getvalue()

    def json_bundle(self):
        with self.db.connect() as db:
            return {
                "summary":self.summary(),
                "devices":[dict(r) for r in db.execute("SELECT * FROM devices ORDER BY id DESC").fetchall()],
                "alerts":[dict(r) for r in db.execute("SELECT * FROM alerts ORDER BY id DESC").fetchall()],
                "incidents":[dict(r) for r in db.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()],
            }
