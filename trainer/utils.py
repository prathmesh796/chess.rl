# trainer/utils.py

import torch
import chess

piece_to_channel = {
    chess.PAWN: 0,
    chess.KNIGHT: 1,
    chess.BISHOP: 2,
    chess.ROOK: 3,
    chess.QUEEN: 4,
    chess.KING: 5,
}

def board_to_tensor(fen):
    board = chess.Board(fen)

    tensor = torch.zeros(12, 8, 8)

    for square, piece in board.piece_map().items():
        row = 7 - (square // 8)
        col = square % 8

        channel = piece_to_channel[piece.piece_type]

        if piece.color == chess.WHITE:
            tensor[channel][row][col] = 1
        else:
            tensor[channel + 6][row][col] = 1

    return tensor