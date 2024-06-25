import asyncio
import websockets
import json
import random

async def send_random_data(websocket, path):
    print(f"Client connected to {path}")
    if path != "/custom-path/":
        return
    try:
        while True:
            data = {'value': random.random()}
            await websocket.send(json.dumps(data))
            await asyncio.sleep(5)
    except websockets.ConnectionClosed:
        print("Client disconnected")

start_server = websockets.serve(send_random_data, "127.0.0.2", 5001)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is running on ws://127.0.0.2:5001/custom-path")
asyncio.get_event_loop().run_forever()
