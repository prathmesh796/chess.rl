# trainer/train.py

import torch
import torch.nn as nn
import torch.optim as optim
import psycopg2
import os
from dotenv import load_dotenv
from model import ChessNet
from utils import board_to_tensor

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

device = torch.device("cpu")

def fetch_data():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute("""
        SELECT fen, reward
        FROM "Move"
        WHERE reward IS NOT NULL
        LIMIT 20000;
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def train():
    data = fetch_data()

    model = ChessNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    policy_loss_fn = nn.CrossEntropyLoss()
    value_loss_fn = nn.MSELoss()

    for epoch in range(5):
        total_loss = 0

        for fen, reward in data:
            board_tensor = board_to_tensor(fen).unsqueeze(0).to(device)

            policy_logits, value_pred = model(board_tensor)

            # Dummy target for now (improve later)
            policy_target = torch.tensor([0]).to(device)

            value_target = torch.tensor([[reward]], dtype=torch.float32).to(device)

            policy_loss = policy_loss_fn(policy_logits, policy_target)
            value_loss = value_loss_fn(value_pred, value_target)

            loss = policy_loss + value_loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch} Loss: {total_loss}")

    torch.save(model.state_dict(), "model_v1.pt")
    print("Model saved as model_v1.pt")


if __name__ == "__main__":
    train()