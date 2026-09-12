# Humanization note: Keep API handlers focused on transport concerns so validation and domain behavior remain reusable elsewhere. The build_router entry point keeps that boundary visible to readers.
from __future__ import annotations
from fastapi import APIRouter, HTTPException, Query, Request, Response
from fastapi.responses import PlainTextResponse, JSONResponse
from app.schemas.observations import ObservationIn
from app.auth.service import COOKIE_NAME, SESSION_MINUTES

def build_router(db, detector, incidents, baseline, audit, interfaces, auth):
    router=APIRouter(prefix="/api")

    @router.get("/auth/status")
    def auth_status(request: Request):
        token = request.cookies.get(COOKIE_NAME)
        current = auth.current_user(token)
        if not current:
            return {"authenticated": False}
        user, _ = current
        return {"authenticated": True, "username": user.username, "display_name": user.display_name,
                "role": user.role, "must_change_password": user.must_change_password,
                "csrf_token": auth.create_csrf_token(token)}

    @router.post("/auth/login")
    async def auth_login(request: Request):
        body = await request.json()
        try:
            user = auth.authenticate(str(body.get("username","")), str(body.get("password","")))
            token, csrf, expires = auth.create_session(user, request.headers.get("user-agent",""))
        except PermissionError as exc:
            return JSONResponse({"error": str(exc)}, status_code=401)
        except ValueError as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        response = JSONResponse({
            "authenticated": True, "username": user.username, "display_name": user.display_name,
            "role": user.role, "must_change_password": user.must_change_password,
            "csrf_token": csrf, "expires_at": expires.isoformat()
        })
        secure = request.url.scheme == "https"
        response.set_cookie(COOKIE_NAME, token, httponly=True, secure=secure,
                            samesite="lax", max_age=SESSION_MINUTES*60, path="/")
        return response

    @router.post("/auth/logout")
    def auth_logout(request: Request, response: Response):
        auth.logout(request.cookies.get(COOKIE_NAME))
        response = JSONResponse({"authenticated": False})
        response.delete_cookie(COOKIE_NAME, path="/")
        return response

    @router.post("/auth/change-password")
    async def auth_change_password(request: Request):
        user = request.state.auth_user
        body = await request.json()
        try:
            auth.change_password(user.id, str(body.get("current_password","")), str(body.get("new_password","")))
        except (PermissionError, ValueError) as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)
        audit.record(user.username, "auth.password.change", "user", user.id, {"result": "success"})
        return {"changed": True}

    @router.get("/auth/me")
    def auth_me(request: Request):
        user = request.state.auth_user
        return {"id": user.id, "username": user.username, "display_name": user.display_name,
                "role": user.role, "must_change_password": user.must_change_password}

    @router.get("/health")
    def health(): return {"status":"ok","database":str(db.path),"version":"2.0.0"}

    @router.get("/health/details")
    def health_details():
        return {
            "status": "ok",
            "service": "netshield-arp-guardian",
            "api": "json",
            "external_api_keys_required": False,
        }

    @router.get("/dashboard")
    def dashboard():
        with db.connect() as c:
            return {
                "devices":c.execute("SELECT COUNT(*) FROM devices").fetchone()[0],
                "events":c.execute("SELECT COUNT(*) FROM arp_events").fetchone()[0],
                "alerts":c.execute("SELECT COUNT(*) FROM alerts WHERE status NOT IN ('resolved','closed','false_positive')").fetchone()[0],
                "critical":c.execute("SELECT COUNT(*) FROM alerts WHERE severity='critical' AND status NOT IN ('resolved','closed')").fetchone()[0],
                "suspicious_events":c.execute("SELECT COUNT(*) FROM arp_events WHERE detection_result='suspicious'").fetchone()[0],
                "recent_events":[dict(r) for r in c.execute("SELECT * FROM arp_events ORDER BY id DESC LIMIT 15").fetchall()],
                "recent_alerts":[dict(r) for r in c.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 10").fetchall()],
            }

    @router.post("/observations")
    async def observations(payload:ObservationIn): return await detector.evaluate(payload)

    @router.get("/devices")
    def devices():
        with db.connect() as c: return [dict(r) for r in c.execute("SELECT * FROM devices ORDER BY last_seen DESC").fetchall()]

    @router.patch("/devices/{device_id}/trust")
    def trust(request:Request, device_id:int):
        with db.connect() as c:
            row=c.execute("SELECT trusted FROM devices WHERE id=?",(device_id,)).fetchone()
            if not row: raise HTTPException(404,"Device not found")
            value=0 if row["trusted"] else 1
            c.execute("UPDATE devices SET trusted=?,status=? WHERE id=?",(value,"trusted" if value else "unknown",device_id))
        audit.record(request.state.auth_user.username,"device.trust.toggle","device",device_id,{"trusted":bool(value)})
        return {"id":device_id,"trusted":bool(value)}

    @router.get("/alerts")
    def alerts(status:str|None=None):
        with db.connect() as c:
            if status:
                rows=c.execute("SELECT * FROM alerts WHERE status=? ORDER BY id DESC",(status,)).fetchall()
            else:
                rows=c.execute("SELECT * FROM alerts ORDER BY id DESC").fetchall()
            return [dict(r) for r in rows]

    @router.post("/alerts/{alert_id}/acknowledge")
    def acknowledge(request:Request, alert_id:int):
        with db.connect() as c:
            row=c.execute("SELECT * FROM alerts WHERE id=?",(alert_id,)).fetchone()
            if not row: raise HTTPException(404,"Alert not found")
            c.execute("UPDATE alerts SET status='acknowledged',acknowledged_at=datetime('now') WHERE id=?",(alert_id,))
            result=c.execute("SELECT * FROM alerts WHERE id=?",(alert_id,)).fetchone()
        audit.record(request.state.auth_user.username,"alert.acknowledge","alert",alert_id)
        return dict(result)

    @router.get("/packets")
    def packets(limit:int=Query(100,ge=1,le=500)):
        with db.connect() as c: return [dict(r) for r in c.execute("SELECT * FROM arp_events ORDER BY id DESC LIMIT ?",(limit,)).fetchall()]

    @router.get("/rules")
    def rules():
        with db.connect() as c: return [dict(r) for r in c.execute("SELECT * FROM detection_rules ORDER BY rule_id").fetchall()]

    @router.get("/baselines")
    def baselines(network_key:str|None=None): return baseline.list(network_key)

    @router.get("/interfaces")
    def interface_list(): return [x.__dict__ for x in interfaces.discover()]

    @router.get("/incidents")
    def incident_list(): return incidents.list()

    @router.get("/incidents/{incident_id}")
    def incident(incident_id:int):
        result=incidents.get(incident_id)
        if not result: raise HTTPException(404,"Incident not found")
        return result

    @router.get("/audit")
    def audit_logs(limit:int=Query(100,ge=1,le=500)): return audit.list(limit)

    @router.get("/reports/summary")
    def report_summary():
        from app.reporting.service import ReportService
        return ReportService(db).summary()

    @router.get("/reports/events.csv",response_class=PlainTextResponse)
    def events_csv():
        from app.reporting.service import ReportService
        return ReportService(db).events_csv()

    return router
