import threading

import customtkinter as ctk
import socketio
import time

# Connect to the WebSocket server
sio = socketio.Client()

# Establish connection
def connect_to_server():
    sio.connect('http://127.0.0.1:5000')

def setup_gui():
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Players")

    def button_event():
        curtime = str(time.time())
        print("button pressed " + curtime)
        graphic_event_payload = {
            "recipient": "test_screen",
            "component": "component1",
            "attribute": "state",
            "parameter": "move100_1"
        }
        sio.emit('relay', graphic_event_payload)

    def button2_event():
        curtime = str(time.time())
        print("button pressed "+curtime)
        graphic_event_payload = {
            "recipient": "test_screen",
            "component": "component1",
            "attribute": "state",
            "parameter": "move100_0"
        }
        sio.emit('relay', graphic_event_payload)

    button = ctk.CTkButton(app, text="State ON", command=button_event)
    button2 = ctk.CTkButton(app, text="State OFF", command=button2_event)
    button.pack(padx=10, pady=10)
    button2.pack(padx=10, pady=10)
    app.mainloop()

# Run the GUI and connect to server in a separate thread
if __name__ == "__main__":
    # Start the Socket.IO connection in a background thread
    threading.Thread(target=connect_to_server).start()

    # Start the customtkinter GUI
    setup_gui()
