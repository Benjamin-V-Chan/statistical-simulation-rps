import networkx as nx
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from utils import MOVES

df = pd.read_csv("data/match_history.csv")

# Compute transition probabilities
transitions = pd.crosstab(df["P1_Move"], df["P2_Move"], normalize="index")

# Plot transition matrix
plt.figure(figsize=(6,6))
sns.heatmap(transitions, annot=True, cmap="coolwarm")
plt.title("Markov Transition Matrix")
plt.savefig("outputs/transition_matrix_heatmap.png")

# Create state transition diagram
G = nx.DiGraph()
for move in MOVES:
    for next_move in MOVES:
        weight = transitions.loc[move, next_move]
        if weight > 0:
            G.add_edge(move, next_move, weight=round(weight, 2))

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, font_size=12)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Markov Chain: Decision Patterns")
plt.savefig("outputs/markov_transition_diagram.png")