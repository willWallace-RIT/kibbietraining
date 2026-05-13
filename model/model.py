import torch
import torch.nn as nn

class KeyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(42, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 26)  # A-Z
        )

    def forward(self, x):
        return self.net(x)
