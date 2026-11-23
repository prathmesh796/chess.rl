import torch
import torch.nn as nn
import torch.nn.functional as F

class ChessNet(nn.Module):
    def __init__(self):
        super().__init__()

        # Shared trunk
        self.conv1 = nn.Conv2d(12, 64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=3, padding=1)

        # Policy head
        self.policy_conv = nn.Conv2d(64, 2, kernel_size=1)
        self.policy_fc = nn.Linear(2 * 8 * 8, 4672)

        # Value head
        self.value_conv = nn.Conv2d(64, 1, kernel_size=1)
        self.value_fc1 = nn.Linear(8 * 8, 128)
        self.value_fc2 = nn.Linear(128, 1)

    def forward(self, x):
        # Shared layers
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))

        # Policy
        p = F.relu(self.policy_conv(x))
        p = p.view(p.size(0), -1)
        p = self.policy_fc(p)

        # Value
        v = F.relu(self.value_conv(x))
        v = v.view(v.size(0), -1)
        v = F.relu(self.value_fc1(v))
        v = torch.tanh(self.value_fc2(v))

        return p, v

class DQNAgent:
    def __init__(self):
        self.model = ChessNet()
        self.model.load_state_dict(torch.load("model_v1.pt"))
        self.model.eval()
        self.epsilon = 0.1

    def select_move(self, board):
        if random.random() < self.epsilon:
            return random.choice(list(board.legal_moves))
        else:
            policy_logits, _ = self.model(board_to_tensor(board.fen()).unsqueeze(0))
            policy = torch.softmax(policy_logits, dim=1).squeeze()
            sorted_indices = torch.argsort(policy, descending=True)
            for index in sorted_indices:
                move = index_to_move(index.item(), board)
                if move is not None:
                    return move
            return random.choice(list(board.legal_moves))