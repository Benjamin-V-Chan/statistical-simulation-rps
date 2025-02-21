# statistical-simulation-rps

## Project Overview

This project is a **highly advanced statistical simulation** of Rock-Paper-Scissors (RPS) strategies, exploring **decision patterns, predictive modeling, and strategy matchups** through various mathematical techniques, including **Markov Chains, Bayesian Inference, Monte Carlo Simulations, Reinforcement Learning, and ELO Rating Systems**.

## Folder Structure

```
project-root/
├── data/                   # Initial datasets
│   ├── match_history.csv   # Simulated match history dataset
│   ├── transition_matrix.csv  # Markov transition probabilities
├── scripts/                # Python scripts for simulation & analysis
│   ├── 01_simulate_matches.py       # Runs RPS simulations with strategies
│   ├── 02_generate_statistics.py    # Generates statistical insights
│   ├── 03_monte_carlo_sim.py        # Monte Carlo simulation for strategy success
│   ├── 04_clustering_analysis.py    # Clusters player behavior using K-Means or DBSCAN
│   ├── 05_reinforcement_learning.py # RL-based strategy evolution
│   ├── 06_markov_analysis.py        # Analyzes decision patterns using Markov chains
│   ├── 07_bayesian_update.py        # Bayesian inference for move probabilities
│   ├── 08_strategy_elo_ratings.py   # ELO rating progression for strategies
│   ├── 09_visualization_dashboard.py # Interactive dashboard using Plotly/Dash
│   ├── utils.py                     # Utility functions for data handling
├── outputs/                # Results & analysis outputs
│   ├── simulation_results.csv
│   ├── strategy_matchup_matrix.png
│   ├── monte_carlo_chart.png
│   ├── clustering_results.png
│   ├── reinforcement_learning_curve.png
│   ├── bayesian_update_viz.png
│   ├── markov_transition_diagram.png
│   ├── strategy_elo_progression.png
│   ├── heatmap_strategy_choices.png
│   ├── transition_matrix_heatmap.png
│   ├── time_series_strategy_performance.png
├── requirements.txt        # Required Python libraries
├── README.md               # Documentation
```

---

## Usage

### **1. Setup the Project:**
Clone the repository.
Ensure you have Python installed.
Install required dependencies using:
```bash
pip install -r requirements.txt
```

### **2. Run Simulation**
Run the Rock-Paper-Scissors strategy simulation:
```bash
python scripts/01_simulate_matches.py
```

### **3. Generate Statistical Insights**
```bash
python scripts/02_generate_statistics.py
```

### **4. Monte Carlo Strategy Evaluation**
```bash
python scripts/03_monte_carlo_sim.py
```

### **5. Clustering Player Behavior**
```bash
python scripts/04_clustering_analysis.py
```

### **6. Reinforcement Learning Strategy Evolution**
```bash
python scripts/05_reinforcement_learning.py
```

### **7. Markov Chain Analysis of Decisions**
```bash
python scripts/06_markov_analysis.py
```

### **8. Bayesian Update of Move Probabilities**
```bash
python scripts/07_bayesian_update.py
```

### **9. Strategy ELO Ratings Over Time**
```bash
python scripts/08_strategy_elo_ratings.py
```

### **10. Interactive Visualization Dashboard**
```bash
python scripts/09_visualization_dashboard.py
```

---

## Requirements

This project requires Python 3.8+ and the following libraries:

```
numpy
pandas
matplotlib
seaborn
scipy
networkx
scikit-learn
trueskill
dash
plotly
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```