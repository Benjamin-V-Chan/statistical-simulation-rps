import numpy as np
import matplotlib.pyplot as plt
import random

ACTIONS = ["Rock", "Paper", "Scissors"]
Q_TABLE = {action: {opponent: 0 for opponent in ACTIONS} for action in ACTIONS}
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 0.2  # Exploration rate
EPISODES = 10000

def get_reward(my_move, opponent_move):
    if my_move == opponent_move:
        return 0
    elif (my_move == "Rock" and opponent_move == "Scissors") or \
         (my_move == "Paper" and opponent_move == "Rock") or \
         (my_move == "Scissors" and opponent_move == "Paper"):
        return 1
    return -1

def choose_action(opponent_move):
    if random.uniform(0, 1) < EPSILON:
        return random.choice(ACTIONS)
    return max(Q_TABLE, key=lambda x: Q_TABLE[x][opponent_move])

# Train the Q-learning agent
rewards = []
for _ in range(EPISODES):
    my_move = random.choice(ACTIONS)
    opponent_move = random.choice(ACTIONS)
    reward = get_reward(my_move, opponent_move)
    best_next = max(Q_TABLE[opponent_move].values())
    Q_TABLE[my_move][opponent_move] += ALPHA * (reward + GAMMA * best_next - Q_TABLE[my_move][opponent_move])
    rewards.append(reward)

# Plot learning curve
plt.plot(np.cumsum(rewards) / np.arange(1, EPISODES + 1))
plt.title("Reinforcement Learning: Q-Learning Strategy Evolution")
plt.savefig("outputs/reinforcement_learning_curve.png")