
# Chess Agent ♟️

An experimental chess-playing AI built using Reinforcement Learning and neural networks. The project explores how an agent can learn to play chess through self-play, generate its own training data, and improve its policy through iterative training.

The goal is to develop a chess agent that learns from experience rather than relying entirely on manually programmed chess strategies.

## Overview

Traditional chess engines rely heavily on handcrafted evaluation functions and search algorithms. This project explores a learning-based approach in which a neural network is trained using games generated through self-play.

The agent follows an iterative learning process:

1. Play chess games through self-play.
2. Collect game positions and corresponding outcomes.
3. Process the generated data into a training dataset.
4. Train a neural network using the collected experience.
5. Use the updated model to generate new games and continue learning.

## Features

- **Reinforcement Learning:** Experimenting with reward-based learning for chess.
- **Self-Play:** Generate chess games by allowing the agent to play against itself.
- **Automated Data Generation:** Build training datasets from simulated games.
- **Neural Network:** Use a PyTorch-based ChessNet model to learn from chess positions.
- **Iterative Training:** Train successive model versions using newly generated experience.
- **CPU-Based Training:** Develop and experiment with the training pipeline without requiring a dedicated GPU.

## Architecture

The project consists of several components:

### 1. Chess Environment

Provides the game state and interaction interface required for the agent to play chess.

The environment is responsible for representing positions, processing moves, and determining game outcomes.

### 2. Self-Play Engine

Runs simulated games between agents using the current model.

Self-play provides an automated way to generate experience without requiring manually collected chess games.

### 3. Data Generation Pipeline

Collects information from simulated games and prepares it for model training.

The generated data can be used to associate chess positions with game outcomes and learning targets.

### 4. Neural Network

A PyTorch-based neural network, ChessNet, is used to learn patterns from chess positions.

The model is trained using data generated from the self-play pipeline.

### 5. Training Pipeline

The training process follows an iterative workflow:

`Model → Self-Play → Dataset → Training → Updated Model`

Each iteration produces a new model version that can be used for subsequent self-play experiments.

## Reinforcement Learning Approach

The project explores reinforcement learning through self-play.

Chess is treated as a sequential decision-making problem in which the agent observes a board position, selects a move, and receives feedback based on the eventual game outcome.

The learning process uses game outcomes as feedback:

- Win: Positive reward
- Loss: Negative reward
- Draw: Neutral reward

The objective is to learn a policy that selects better moves over repeated training iterations.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| PyTorch | Neural network development and training |
| Reinforcement Learning | Agent learning framework |
| Self-Play | Automated experience generation |

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd chess-agent
```

Create and activate a virtual environment.

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

Run the appropriate self-play, data generation, or training entrypoint from the repository.

The exact script names and arguments depend on the current implementation.

## Training Experiments

The project uses versioned models to support iterative experimentation.

For example:

- `model_v1`: Initial model trained using generated self-play experience.
- `model_v2`: Updated model trained using additional experience generated from the previous iteration.

The purpose of model versioning is to track training progress and compare the behavior of successive models.

## Current Status

This project is under active experimentation.

Current focus areas include:

- Improving the quality of self-play games.
- Refining the chess position representation.
- Improving neural network training.
- Developing more effective data generation strategies.
- Evaluating model performance across training iterations.

## Future Improvements

- Implement stronger policy and value network architectures.
- Explore Monte Carlo Tree Search (MCTS).
- Improve training stability and sample efficiency.
- Add automated model evaluation and benchmarking.
- Compare successive models against baseline chess-playing agents.
- Develop an interactive interface to play against the trained agent.

## Learning Resources

This project is inspired by reinforcement learning concepts including:

- Self-play
- Policy learning
- Reward-based optimization
- Neural network function approximation
- Iterative improvement through generated experience

## Contributing

Contributions, suggestions, and discussions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a pull request describing the improvement.