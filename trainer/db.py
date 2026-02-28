# trainer/db.py

import requests

API_URL = "http://localhost:3000/api/selfplay"

def create_game(model_version):
    res = requests.post(API_URL, json={
        "type": "create_game",
        "payload": { "modelVersion": model_version }
    })
    return res.json()["gameId"]


def insert_move(game_id, move_index, fen, move_uci, player):
    requests.post(API_URL, json={
        "type": "insert_move",
        "payload": {
            "gameId": game_id,
            "moveIndex": move_index,
            "fen": fen,
            "moveUci": move_uci,
            "player": player
        }
    })


def update_rewards(game_id, winner):
    requests.post(API_URL, json={
        "type": "update_rewards",
        "payload": {
            "gameId": game_id,
            "winner": winner
        }
    })