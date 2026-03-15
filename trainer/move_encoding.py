import chess

DIRECTIONS = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

KNIGHT_MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

PROMOTIONS = [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]


def safe_direction(delta_rank, delta_file):
    dr = 0 if delta_rank == 0 else delta_rank // abs(delta_rank)
    df = 0 if delta_file == 0 else delta_file // abs(delta_file)
    return dr, df


def move_to_index(move: chess.Move):
    from_square = move.from_square
    to_square = move.to_square

    from_rank = chess.square_rank(from_square)
    from_file = chess.square_file(from_square)

    to_rank = chess.square_rank(to_square)
    to_file = chess.square_file(to_square)

    delta_rank = to_rank - from_rank
    delta_file = to_file - from_file

    # ---- Knight moves ----
    if (delta_rank, delta_file) in KNIGHT_MOVES:
        move_type = KNIGHT_MOVES.index((delta_rank, delta_file))
        return from_square * 73 + move_type

    # ---- Promotions ----
    if move.promotion:
        direction = safe_direction(delta_rank, delta_file)

        if direction in DIRECTIONS:
            dir_index = DIRECTIONS.index(direction)
            promo_index = PROMOTIONS.index(move.promotion)

            move_type = 56 + dir_index * 4 + promo_index
            return from_square * 73 + move_type

    # ---- Sliding moves ----
    direction = safe_direction(delta_rank, delta_file)

    if direction in DIRECTIONS:
        dir_index = DIRECTIONS.index(direction)
        distance = max(abs(delta_rank), abs(delta_file)) - 1
        move_type = 8 + dir_index * 7 + distance
        return from_square * 73 + move_type

    raise ValueError(f"Unsupported move: {move}")


def index_to_move(index, board):
    legal_moves = list(board.legal_moves)

    for move in legal_moves:
        try:
            if move_to_index(move) == index:
                return move
        except:
            continue

    return None