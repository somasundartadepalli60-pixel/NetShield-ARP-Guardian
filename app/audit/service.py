# Humanization note: Record security-relevant decisions separately from operational logs so the audit trail remains useful. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
import json
from datetime import datetime, timezone

class AuditService:
    def __init__(self, db):
        self.db=db
    def record(self, actor, action, resource_type, resource_id=None, details=None):
        with self.db.connect() as db:
            db.execute("""INSERT INTO audit_logs(actor,action,resource_type,resource_id,details,created_at)
                          VALUES(?,?,?,?,?,?)""",
                       (actor,action,resource_type,str(resource_id) if resource_id is not None else None,
                        json.dumps(details or {},default=str),datetime.now(timezone.utc).isoformat()))
    def list(self, limit=200):
        limit=max(1,min(int(limit),500))
        with self.db.connect() as db:
            return [dict(r) for r in db.execute("SELECT * FROM audit_logs ORDER BY id DESC LIMIT ?",(limit,)).fetchall()]
