import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import chess
import random
import json
from tqdm import tqdm
from datetime import datetime

NUM_GAMES = 1000
MAX_MOVES = 80
MODEL_VERSION = "v0"

def play_game(game_id):
    board = chess.Board()
    moves = []

    move_index = 0

    while not board.is_game_over() and move_index < MAX_MOVES:
        fen = board.fen()
        move = random.choice(list(board.legal_moves))
        player = "white" if board.turn else "black"

        moves.append({
            "game_id": game_id,
            "move_index": move_index,
            "fen": fen,
            "move": move.uci(),
            "player": player
        })

        board.push(move)
        move_index += 1

    result = board.result()

    final_value = 0

    if result == "1-0":
        final_value = 1
    elif result == "0-1":
        final_value = -1

    for move in moves:
        move["reward"] = final_value

    return {
        "game_id": game_id,
        "model_version": MODEL_VERSION,
        "result": result,
        "moves": moves
    }


if __name__ == "__main__":
    all_games = []

    for game_num in tqdm(range(NUM_GAMES)):
        game_data = play_game(game_num)
        all_games.append(game_data)

    filename = f"self_play_{MODEL_VERSION}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(BASE_DIR, "data", filename)

    with open(filepath, "w") as f:
        json.dump(all_games, f)

    print(f"Saved {NUM_GAMES} games to {filepath}")