# Humanization note: Treat baselines as historical context rather than unquestioned truth; networks legitimately change over time. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
from datetime import datetime, timezone

class BaselineService:
    def __init__(self, db):
        self.db=db

    def observe(self, network_key, ip_address, mac_address):
        now=datetime.now(timezone.utc).isoformat()
        with self.db.connect() as db:
            row=db.execute("""SELECT id,observations,confidence FROM baselines
                              WHERE network_key=? AND ip_address=? AND mac_address=?""",
                           (network_key,ip_address,mac_address)).fetchone()
            if row:
                observations=row["observations"]+1
                confidence=min(.99, .50 + observations/200)
                db.execute("""UPDATE baselines SET observations=?,confidence=?,last_seen=? WHERE id=?""",
                           (observations,confidence,now,row["id"]))
                return {"id":row["id"],"observations":observations,"confidence":confidence}
            cur=db.execute("""INSERT INTO baselines(network_key,ip_address,mac_address,observations,confidence,first_seen,last_seen)
                              VALUES(?,?,?,?,?,?,?)""",(network_key,ip_address,mac_address,1,.51,now,now))
            return {"id":cur.lastrowid,"observations":1,"confidence":.51}

    def list(self, network_key=None):
        with self.db.connect() as db:
            if network_key:
                rows=db.execute("SELECT * FROM baselines WHERE network_key=? ORDER BY last_seen DESC",(network_key,)).fetchall()
            else:
                rows=db.execute("SELECT * FROM baselines ORDER BY last_seen DESC").fetchall()
            return [dict(r) for r in rows]
