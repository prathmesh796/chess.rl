import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from model import ChessNet
from dataset import ChessDataset

device = torch.device("cpu")

def train():
    print("Loading dataset...")
    data = torch.load(os.path.join(os.path.dirname(__file__), "data", "dataset.pt"))

    dataset = ChessDataset(data)
    loader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = ChessNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    policy_loss_fn = nn.CrossEntropyLoss()
    value_loss_fn = nn.MSELoss()

    print("Starting training...")

    for epoch in range(5):
        total_loss = 0

        for boards, move_indices, rewards in loader:
            boards = boards.to(device)
            move_indices = move_indices.to(device)
            rewards = rewards.to(device)

            policy_logits, value_pred = model(boards)

            policy_loss = policy_loss_fn(policy_logits, move_indices)
            value_loss = value_loss_fn(value_pred.squeeze(), rewards)

            loss = policy_loss + value_loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1} | Loss: {total_loss:.4f}")

    torch.save(model.state_dict(), os.path.join(os.path.dirname(__file__), "models", "model_v1.pt"))
    print("Model saved as model_v1.pt")


if __name__ == "__main__":
    train()