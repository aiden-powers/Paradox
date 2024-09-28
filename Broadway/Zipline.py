from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

players = {
        "player1": {"username": "Username1", "character": "None"},
        "player2": {"username": "Username2", "character": "None"},
        "player3": {"username": "Username3", "character": "None"},
        "player4": {"username": "Username4", "character": "None"},
        "player5": {"username": "Username5", "character": "None"},
        "player6": {"username": "Username6", "character": "None"},
        "player7": {"username": "Username7", "character": "None"},
        "player8": {"username": "Username8", "character": "None"},
        "player9": {"username": "Username9", "character": "None"},
        "player10": {"username": "Username10", "character": "None"},
        "player11": {"username": "Username11", "character": "None"},
        "player12": {"username": "Username12", "character": "None"},
}

@app.route("/players")
def hello_world():
    return jsonify(players)

# WebSocket event to send the teams data on connection
@socketio.on('connect')
def handle_connect():
    emit('players', players)

# WebSocket event to update individual player data
@socketio.on('update_player')
def update_player(data):
    global players
    player_key = data.get('player')
    player_data = data.get('player_data')
    players[player_key].update(player_data)
    emit('players', players, broadcast=True)
    print(players)



if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
