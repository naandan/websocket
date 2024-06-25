from flask import Flask
import asyncio
import websockets
import json
import random
from threading import Thread

app = Flask(__name__)

async def send_random_data(websocket, path):
    print(f"Client connected to {path}")
    try:
        while True:
            data = {'value': random.random()}
            await websocket.send(json.dumps(data))
            await asyncio.sleep(5)  # Mengirim data setiap 5 detik
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def websocket_handler():
    async with websockets.serve(send_random_data, "localhost", 5001):
        await asyncio.Future()  # Run forever

@app.route('/')
def index():
    return "Flask server is running"

if __name__ == '__main__':
    websocket_thread = Thread(target=lambda: asyncio.run(websocket_handler()))
    websocket_thread.start()
    app.run(host='0.0.0.0', port=5000)
