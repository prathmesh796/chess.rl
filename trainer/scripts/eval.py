import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import torch
import chess
import random
from network.model import ChessNet
from utils.utils import board_to_tensor
from utils.move_encoding import index_to_move

device = torch.device("cpu")

def select_model_move(model, board):
    model.eval()

    board_tensor = board_to_tensor(board.fen()).unsqueeze(0).to(device)

    with torch.no_grad():
        policy_logits, _ = model(board_tensor)

    policy = torch.softmax(policy_logits, dim=1).squeeze()

    # Sort indices from best to worst
    sorted_indices = torch.argsort(policy, descending=True)

    for index in sorted_indices:
        move = index_to_move(index.item(), board)
        if move is not None:
            return move

    # Fallback
    return random.choice(list(board.legal_moves))


def play_game(model):
    board = chess.Board()

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = select_model_move(model, board)
        else:
            move = random.choice(list(board.legal_moves))

        board.push(move)

    return board.result()


def evaluate():
    model = ChessNet()
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    model.load_state_dict(torch.load(os.path.join(BASE_DIR, "models", "model_v1.pt"), map_location=device))
    model.to(device)

    wins = 0
    losses = 0
    draws = 0

    games = 20

    for _ in range(games):
        result = play_game(model)

        if result == "1-0":
            wins += 1
        elif result == "0-1":
            losses += 1
        else:
            draws += 1

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")


if __name__ == "__main__":
    evaluate()