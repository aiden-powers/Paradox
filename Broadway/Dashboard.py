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

# Set up the GUI using customtkinter
def setup_gui():
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Players")

    # Username entry
    username_label = ctk.CTkLabel(app, text="Username:")
    username_label.pack(pady=10)
    username_entry = ctk.CTkEntry(app, placeholder_text="Enter Username")
    username_entry.pack(pady=10)

    # Character entry
    character_label = ctk.CTkLabel(app, text="Character:")
    character_label.pack(pady=10)
    character_entry = ctk.CTkOptionMenu(app, values=Characters.characterlist)
    character_entry.pack(pady=10)

    # Player selection dropdown
    player_label = ctk.CTkLabel(app, text="Select Player:")
    player_label.pack(pady=10)
    player_dropdown = ctk.CTkOptionMenu(app, values=["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "player9", "player10", "player11", "player12"])
    player_dropdown.pack(pady=10)

    # Update button
    def update_team():
        player = player_dropdown.get()
        username = username_entry.get()
        character = character_entry.get()
        update_server_data(player, username, character)

    update_button = ctk.CTkButton(app, text="Update", command=update_team)

    update_button.pack(pady=20)

    app.mainloop()

# Run the GUI and connect to server in a separate thread
if __name__ == "__main__":
    # Start the Socket.IO connection in a background thread
    threading.Thread(target=connect_to_server).start()

    # Start the customtkinter GUI
    setup_gui()
