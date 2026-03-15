import json
import torch
import os
from utils import board_to_tensor


def preprocess_and_save():
    with open(os.path.join(os.path.dirname(__file__), "data", "training_data.json"), "r") as f:
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

    torch.save(processed_data, os.path.join(os.path.dirname(__file__), "data", "dataset.pt"))
    print(f"Saved {len(processed_data)} samples to dataset.pt")


if __name__ == "__main__":
    preprocess_and_save()