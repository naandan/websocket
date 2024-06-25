from flask import Flask
from flask_socketio import SocketIO, Namespace
import random
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

class CustomNamespace(Namespace):
    def on_connect(self):
        print('Client connected to custom namespace')

    def on_disconnect(self):
        print('Client disconnected from custom namespace')

# Daftarkan namespace pada path /custom-path
socketio.on_namespace(CustomNamespace('/custom-path'))

def send_random_data():
    while True:
        time.sleep(5)  # Mengirim data setiap 5 detik
        data = {'value': random.random()}
        socketio.emit('updateForm', data, namespace='/custom-path')

@app.route('/')
def index():
    return "WebSocket Server with Custom Path is running"

if __name__ == '__main__':
    thread = Thread(target=send_random_data)
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
