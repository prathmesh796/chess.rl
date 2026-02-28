# trainer/self_play.py

import chess
import random
from tqdm import tqdm
from db import create_game, insert_move, update_rewards

NUM_GAMES = 1000
MODEL_VERSION = "v0"

def play_game():
    board = chess.Board()
    game_id = create_game(MODEL_VERSION)

    move_index = 0

    while not board.is_game_over():
        fen = board.fen()
        move = random.choice(list(board.legal_moves))

        player = "white" if board.turn else "black"

        insert_move(
            game_id,
            move_index,
            fen,
            move.uci(),
            player
        )

        board.push(move)
        move_index += 1

    result = board.result()

    if result == "1-0":
        update_rewards(game_id, "white")
    elif result == "0-1":
        update_rewards(game_id, "black")
    else:
        update_rewards(game_id, "draw")


if __name__ == "__main__":
    for _ in tqdm(range(NUM_GAMES)):
        play_game()

    print("Self-play generation complete.")