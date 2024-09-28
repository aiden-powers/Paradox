import socketio

# Create a SocketIO client
sio = socketio.Client()

# Define event handler for connection
@sio.event
def connect():
    print("Connected to server!")

    # Example update to a player in teamYellow (player1's username and character are updated)
    player_update = {
        "player": "player2",
        "player_data": {
            "username": "NewUsernameExample",
            "character": "Lash"
        }
    }

    # Send the update to the server
    sio.emit('update_player', player_update)


# Define event handler for receiving updated team data
@sio.on('team_data')
def on_team_data(data):
    print("Received updated team data:")
    print(data)


# Define event handler for errors
@sio.on('error')
def on_error(data):
    print("Error:", data)


# Define event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from server.")

def connect_to_server():
    sio.connect('http://127.0.0.1:5000')

connect_to_server()

sio.wait()
