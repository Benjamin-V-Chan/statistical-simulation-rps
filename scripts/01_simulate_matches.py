import csv
from utils import *

# Simulate a game
def simulate_game(strategy1, strategy2, num_rounds=1000):
    history = []
    p1_last_move, p2_last_move = None, None

    for _ in range(num_rounds):
        p1_move = strategy1(p1_last_move)
        p2_move = strategy2(p2_last_move)

        result = determine_winner(p1_move, p2_move)
        history.append((p1_move, p2_move, result))

        p1_last_move, p2_last_move = p1_move, p2_move

    return history

# Save results
def save_results_to_csv(data, filename="data/match_history.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["P1_Move", "P2_Move", "Result"])
        writer.writerows(data)

if __name__ == "__main__":
    results = simulate_game(random_strategy, tit_for_tat, 10000)
    save_results_to_csv(results)