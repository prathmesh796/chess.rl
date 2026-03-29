import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import json
from tqdm import tqdm
from database.db import create_game, insert_bulk_moves

FILENAME = "self_play_v0_20260301_222146.json"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILEPATH = os.path.join(BASE_DIR, "data", FILENAME)

with open(FILEPATH, "r") as f:
    games = json.load(f)

for game in tqdm(games):

    # Create game in DB
    db_game_id = create_game(game["model_version"], game["result"])

    formatted_moves = []

    for move in game["moves"]:
        formatted_moves.append({
            "gameId": db_game_id,
            "moveIndex": move["move_index"],
            "fen": move["fen"],
            "moveUci": move["move"],
            "player": move["player"],
            "reward": move["reward"]
        })

    insert_bulk_moves(formatted_moves)

print("Upload complete.")