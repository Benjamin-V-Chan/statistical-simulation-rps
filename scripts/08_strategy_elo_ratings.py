import trueskill
import matplotlib.pyplot as plt
import random

env = trueskill.TrueSkill(draw_probability=0.1)
strategy_ratings = {s: env.create_rating() for s in ["Random", "Tit-for-Tat", "Markov", "Win-Stay-Lose-Shift"]}

matchups = [("Random", "Tit-for-Tat"), ("Markov", "Win-Stay-Lose-Shift"), ("Random", "Markov")]

elo_history = {s: [] for s in strategy_ratings}
for _ in range(1000):
    for strat1, strat2 in matchups:
        outcome = random.choice([-1, 0, 1])
        if outcome == 1:
            strategy_ratings[strat1], strategy_ratings[strat2] = env.rate_1vs1(strategy_ratings[strat1], strategy_ratings[strat2])
        elif outcome == -1:
            strategy_ratings[strat2], strategy_ratings[strat1] = env.rate_1vs1(strategy_ratings[strat2], strategy_ratings[strat1])
        for strat in strategy_ratings:
            elo_history[strat].append(strategy_ratings[strat].mu)

# Plot ELO progression
for strat, history in elo_history.items():
    plt.plot(history, label=strat)
plt.legend()
plt.title("ELO Rating Evolution for Strategies")
plt.savefig("outputs/strategy_elo_progression.png")
