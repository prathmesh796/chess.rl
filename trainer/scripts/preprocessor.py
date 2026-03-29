import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import json
import torch
from utils.utils import board_to_tensor


def preprocess_and_save():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(BASE_DIR, "data", "training_data.json"), "r") as f:
        rows = json.load(f)

    processed_data = []

    for row in rows:
        fen = row["fen"]
        reward = row["reward"]
        move_index = row["moveIndex"]

        board_tensor = board_to_tensor(fen)

        processed_data.append(
            (
                board_tensor,
                move_index,
                reward
            )
        )

    torch.save(processed_data, os.path.join(BASE_DIR, "data", "dataset.pt"))
    print(f"Saved {len(processed_data)} samples to dataset.pt")


if __name__ == "__main__":
    preprocess_and_save()