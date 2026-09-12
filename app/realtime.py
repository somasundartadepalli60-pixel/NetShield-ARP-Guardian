# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The __init__ entry point keeps that boundary visible to readers.
import asyncio, json
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self): self.connections:set[WebSocket]=set()
    async def connect(self, websocket): await websocket.accept(); self.connections.add(websocket)
    def disconnect(self, websocket): self.connections.discard(websocket)
    async def broadcast(self,event):
        if not self.connections: return
        payload=json.dumps(event,default=str)
        sockets=tuple(self.connections)
        results=await asyncio.gather(*(s.send_text(payload) for s in sockets),return_exceptions=True)
        for s,r in zip(sockets,results):
            if isinstance(r,Exception): self.disconnect(s)
