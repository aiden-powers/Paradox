import customtkinter as ctk
import socketio
import threading
import Characters
import requests

# Connect to the WebSocket server
sio = socketio.Client()

# Define functions for sending updates to the server
def update_server_data(player, username, character):
    player_update = {
        "player": player,
        "player_data": {
            "username": username,
            "character": character
        }
    }
    sio.emit('update_player', player_update)

# Connect to the server
@sio.event
def connect():
    print('Connected to server!')

# Function to listen to updates from the server
@sio.on('team_data')
def on_team_data(data):
    print('Received updated data from server:', data)

# Establish connection
def connect_to_server():
    sio.connect('http://127.0.0.1:5000')

def setup_gui():
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Players")

    for i in range(1, 7):
        character_entry = ctk.CTkOptionMenu(app, values=Characters.characterlist, command=lambda i=i: print(f"Player {i}"))
        character_entry.pack(side="left", padx=5)
    app.mainloop()

# Run the GUI and connect to server in a separate thread
if __name__ == "__main__":
    # Start the Socket.IO connection in a background thread
    threading.Thread(target=connect_to_server).start()

    # Start the customtkinter GUI
    setup_gui()
