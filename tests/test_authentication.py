from fastapi.testclient import TestClient
from app.main import app, database

def test_login_sets_authenticated_session():
    database.initialize()
    with TestClient(app) as client:
        r=client.post("/api/auth/login",json={"username":"admin","password":"ChangeMe-NetShield-2026!"})
        assert r.status_code==200
        assert r.json()["authenticated"] is True
        assert r.json()["csrf_token"]
        me=client.get("/api/auth/me")
        assert me.status_code==200
        assert me.json()["username"]=="admin"

def test_protected_mutation_requires_csrf():
    database.initialize()
    with TestClient(app) as client:
        r=client.post("/api/auth/login",json={"username":"admin","password":"ChangeMe-NetShield-2026!"})
        assert r.status_code==200
        payload={"source_ip":"10.0.0.20","source_mac":"aa:bb:cc:dd:ee:20",
                 "target_ip":"10.0.0.21","target_mac":"aa:bb:cc:dd:ee:21",
                 "operation":"reply","interface":"auth-test"}
        blocked=client.post("/api/observations",json=payload)
        assert blocked.status_code==403
