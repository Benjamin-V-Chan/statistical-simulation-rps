import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/match_history.csv")

# Compute win rates
win_rate = df.groupby("P1_Move")["Result"].value_counts(normalize=True).unstack()

# Generate heatmap
plt.figure(figsize=(8,6))
sns.heatmap(win_rate, annot=True, cmap="coolwarm")
plt.title("Win Rate Heatmap")
plt.savefig("outputs/heatmap_strategy_choices.png")