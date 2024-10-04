import threading
import socketio
import time

# Connect to the WebSocket server
sio = socketio.Client()

# Establish connection
def connect_to_server():
    sio.connect('http://127.0.0.1:5000')

# Function to send the state ON message
def send_state_on():
    curtime = str(time.time())
    print("Sending State ON at " + curtime)
    graphic_event_payload = {
        "recipient": "test_screen",
        "component": "component1",
        "attribute": "state",
        "parameter": "move100_1"
    }
    sio.emit('relay', graphic_event_payload)

# Function to send the state OFF message
def send_state_off():
    curtime = str(time.time())
    print("Sending State OFF at " + curtime)
    graphic_event_payload = {
        "recipient": "test_screen",
        "component": "component1",
        "attribute": "state",
        "parameter": "move100_0"
    }
    sio.emit('relay', graphic_event_payload)

def send_custom():
    curtime = str(time.time())
    print("Sending Custom at " + curtime)
    graphic_event_payload = {
        "recipient": "test_screen",
        "component": "component1",
        "attribute": "text",
        "parameter": '0.5s cubic-bezier(1, 0, 0, 1)'
    }
    sio.emit('relay', graphic_event_payload)

# Run the Socket.IO connection in a separate thread
if __name__ == "__main__":
    threading.Thread(target=connect_to_server).start()
    time.sleep(2)
    send_custom()
