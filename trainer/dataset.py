import torch
from torch.utils.data import Dataset


class ChessDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        board, move_index, reward = self.data[idx]

        return (
            board.float(),
            torch.tensor(move_index, dtype=torch.long),
            torch.tensor(reward, dtype=torch.float32),
        )