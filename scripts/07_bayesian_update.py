import numpy as np
import matplotlib.pyplot as plt
from utils import MOVES

prior = np.array([1, 1, 1], dtype=float)  # Uniform prior
posteriors = []
move_counts = np.array([0, 0, 0], dtype=float)  # Track counts for empirical likelihood

# Simulated opponent moves
moves = np.random.choice(MOVES, size=100, p=[0.33, 0.33, 0.34])

for move in moves:
    move_idx = MOVES.index(move)
    move_counts[move_idx] += 1  # Track occurrences

    # Empirical likelihood (normalized frequency)
    likelihood = (move_counts + 1) / (move_counts.sum() + len(MOVES))  # Laplace smoothing

    # Bayesian update
    posterior = prior * likelihood
    posterior /= posterior.sum()
    
    posteriors.append(posterior.copy())
    prior = posterior  # Update prior for next step

# Plot Bayesian updates
plt.plot(posteriors)
plt.legend(MOVES)
plt.title("Bayesian Update: Move Probability Predictions")
plt.savefig("outputs/bayesian_update_viz.png")