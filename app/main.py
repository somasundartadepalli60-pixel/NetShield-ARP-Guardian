# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The validation_error_handler entry point keeps that boundary visible to readers.
from pathlib import Path
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from app.config import APP_NAME, VERSION, DB_PATH
from app.db.database import Database
from app.realtime import ConnectionManager
from app.services.detection_service import DetectionService
from app.incidents.service import IncidentService
from app.baselines.service import BaselineService
from app.audit.service import AuditService
from app.network.interfaces import InterfaceDiscovery
from app.api.routes import build_router

database=Database(DB_PATH)
manager=ConnectionManager()
detector=DetectionService(database,manager)
incidents=IncidentService(database)
baseline=BaselineService(database)
audit=AuditService(database)
interfaces=InterfaceDiscovery()

app=FastAPI(title=APP_NAME,version=VERSION,description="Local ARP spoofing detection and network security console.")
STATIC_DIR=Path(__file__).parent/"static"
app.mount("/static",StaticFiles(directory=STATIC_DIR),name="static")
app.include_router(build_router(database,detector,incidents,baseline,audit,interfaces))


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc):
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=422,
            content={"error": "validation_error", "detail": exc.errors()},
        )
    return JSONResponse(status_code=422, content={"error": "validation_error"})

@app.exception_handler(Exception)
async def api_exception_handler(request, exc):
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=500,
            content={"error": "internal_server_error", "detail": str(exc)},
        )
    raise exc

@app.on_event("startup")
def startup(): database.initialize()

@app.get("/",include_in_schema=False)
def index(): return FileResponse(STATIC_DIR/"index.html")

@app.websocket("/ws")
async def websocket(websocket:WebSocket):
    await manager.connect(websocket)
    try:
        while True: await websocket.receive_text()
    except WebSocketDisconnect: manager.disconnect(websocket)
