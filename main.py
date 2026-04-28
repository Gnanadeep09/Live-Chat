from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from database import SessionLocal, ChatMessage

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    with open("index.html") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    db = SessionLocal()
    
    try:
        history = db.query(ChatMessage).order_by(ChatMessage.id.desc()).limit(20).all()
        for msg in reversed(history):
            await websocket.send_text(f"{msg.user}: {msg.content}")

        while True:
            data = await websocket.receive_text()
            new_msg = ChatMessage(user=username, content=data)
            db.add(new_msg)
            db.commit()
            await manager.broadcast(f"{username}: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"📢 {username} left the chat.")
    finally:
        db.close()