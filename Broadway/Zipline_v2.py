from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('relay')
def handle_relay(data):
    emit('graphics_events', data, broadcast=True)

#if __name__ == "__main__":
def begin_thread():
    threading.Thread(socketio.run(app, debug=True, allow_unsafe_werkzeug=True)).start()

