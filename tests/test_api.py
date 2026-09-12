from fastapi.testclient import TestClient
from app.main import app, database

def test_health():
    database.initialize()
    with TestClient(app) as client:
        response=client.get("/api/health")
        assert response.status_code==200
        assert response.json()["status"]=="ok"

def test_observation_round_trip():
    database.initialize()
    with TestClient(app) as client:
        payload={"source_ip":"10.0.0.1","source_mac":"aa:bb:cc:dd:ee:01","target_ip":"10.0.0.2",
                 "target_mac":"aa:bb:cc:dd:ee:02","operation":"reply","interface":"test0"}
        login=client.post("/api/auth/login",json={"username":"admin","password":"ChangeMe-NetShield-2026!"})
        assert login.status_code==200
        client.headers.update({"X-CSRF-Token":login.json()["csrf_token"]})
        response=client.post("/api/observations",json=payload)
        assert response.status_code==200
        body=response.json()
        assert "risk_score" in body and "detector_ids" in body
