from utils import *
import matplotlib.pyplot as plt

# Monte Carlo Simulation
num_simulations = 1000
results = []

for _ in range(num_simulations):
    wins = sum(determine_winner(random_strategy(), tit_for_tat()) == "win" for _ in range(100))
    results.append(wins / 100)

# Plot results
plt.plot(range(num_simulations), results)
plt.title("Monte Carlo Simulation of Strategy Success")
plt.savefig("outputs/monte_carlo_chart.png")