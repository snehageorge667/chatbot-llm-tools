from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from backend.controller import route_message

app = FastAPI()

@app.websocket("/ws/chat")
async def chat_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            user_text = await websocket.receive_text()
            reply = await route_message(user_text)
            await websocket.send_text(reply)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        await websocket.send_text(f"< Error: {str(e)} >")
