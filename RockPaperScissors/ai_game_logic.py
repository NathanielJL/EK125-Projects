"""
Author: Nathaniel Lee
Module: ai_game_logic
Description: Handles AI opponents with different difficulty levels.
"""

"""
Student A: Core Game Logic & AI
- Implement basic rock-paper-scissors rules
- Random AI (completely random choices)
- Pattern AI (looks for player patterns in last 3–5 moves)
- Counter AI (plays what would beat player’s most common choice)
- Input validation for player choices
"""

import random
import os

def play_single_game(ai_difficulty, player_history):
    "Play a single game and update the standardized history list."
    player_move = get_player_move()
    
    ai_move = get_ai_move(ai_difficulty, player_history)
    player_history.append(player_move) 
    result = determine_winner(player_move, ai_move)
    print(f"\nAI played: {ai_move.upper()}")
    print(f"Result: {result.upper()}")
    print("")
    print("=" * 50)
    return result

def get_player_move():
    "Get validated player move from user input."
    valid_moves = ['rock', 'paper', 'scissors']
    
    while True:
        print("\nYour options: rock, paper, scissors")
        user_input = input("Enter your move: ").lower().strip()
        
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue

        if user_input in valid_moves:
            return user_input
        
        print(f"\tInvalid move: '{user_input}'")
        print(f"\tValid moves are: {', '.join(valid_moves)}")
        print("\tPlease try again.")

def get_ai_move(difficulty, player_history=None):
    "Get AI move based on difficulty level."
    if player_history is None:
        player_history = []

    from boss_ai_logic import boss_ai

    if difficulty == 'easy':
        return easy_ai(player_history)
    elif difficulty == 'medium':
        return medium_ai(player_history)
    elif difficulty == 'hard':
        return hard_ai(player_history)
    elif difficulty == 'boss':
        return boss_ai(player_history)
    else:
        return easy_ai(player_history)

def easy_ai(player_history=None):
    "Random AI - completely random choices."
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

def medium_ai(player_history):
    "Pattern AI - looks for patterns in player's last 3-5 moves"
    if player_history is None or len(player_history) < 2:
        return easy_ai() 
    
    recent_moves = player_history[-5:]
    move_counts = {'rock': 0, 'paper': 0, 'scissors': 0}

    for move in recent_moves:
        if move in move_counts:
            move_counts[move] += 1
    
    most_common_move = max(move_counts, key=move_counts.get)
    most_common_count = move_counts[most_common_move]
    
    if most_common_count >= 2:
        return get_counter_move(most_common_move)
    else:
        return easy_ai()

def hard_ai(player_history):
    "Counter AI - plays what would beat player's most common choice overall."
    if player_history is None or len(player_history) == 0:
        return easy_ai()
    
    move_counts = {'rock': 0, 'paper': 0, 'scissors': 0}
    
    for move in player_history:
        if move in move_counts:
            move_counts[move] += 1
    
    most_common_move = max(move_counts, key=move_counts.get)
    return get_counter_move(most_common_move)

def get_counter_move(move):
    "Get the move that beats the given move."
    counters = {
        'rock': 'paper',      
        'paper': 'scissors',  
        'scissors': 'rock'    
    }
    return counters.get(move, 'rock')

def determine_winner(player_move, ai_move):
    "Determine winner of a single round."
    if player_move == ai_move:
        return 'tie'
    
    if player_move == 'rock' and ai_move == 'scissors':
        return 'win'
    if player_move == 'scissors' and ai_move == 'paper':
        return 'win'
    if player_move == 'paper' and ai_move == 'rock':
        return 'win'
    return 'loss'