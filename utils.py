import random

# Define RPS moves
MOVES = ["Rock", "Paper", "Scissors"]

# Determine winner
def determine_winner(move1, move2):
    if move1 == move2:
        return "draw"
    elif (move1, move2) in [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")]:
        return "win"
    return "loss"

# Define strategies
def tit_for_tat(opponent_last_move):
    return opponent_last_move if opponent_last_move else random.choice(MOVES)

def random_strategy():
    return random.choice(MOVES)

def win_stay_lose_shift(prev_move, prev_outcome):
    if prev_outcome == "win":
        return prev_move
    return random.choice(MOVES)