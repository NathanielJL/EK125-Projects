"""
Author: Nathaniel Lee
Module: boss_ai_logic
Description: Q-Learning Boss AI for rock-paper-scissors.
"""
import numpy as np
import os
import json

moves = ['rock', 'paper', 'scissors']
move_to_number = {'rock': 0, 'paper': 1, 'scissors': 2}
save_file = "boss_ai_model.json"
learning_rate = 0.6
discount = 0.9
random_choice = 0.15
win_reward =  1.0
tie_reward =  -0.3
loss_reward = -1.0

num_situations = 9   
num_responses  = 3   


def load_q_table():
    """Load the AI's learned scores from disk."""
    if os.path.exists(save_file):
        try:
            with open(save_file, 'r') as f:
                data = json.load(f)
            q_table = np.array(data["q_table"], dtype=float)
            if q_table.shape == (num_situations, num_responses):
                return q_table
        except (json.JSONDecodeError, KeyError, ValueError):
            print("[Boss AI] Save file was unreadable. Starting fresh.")

    return np.zeros((num_situations, num_responses), dtype=float)

def write_q_table(q_table):
    """""Save the AI's learned scores to disk so they survive between sessions."""
    temp_file = save_file + ".tmp"
    with open(temp_file, 'w') as f:
        json.dump({"q_table": q_table.tolist()}, f, indent=2)
    os.replace(temp_file, save_file)

def get_situation(player_history):
    """Turn the player's last 2 moves into a single row number for the Q-table."""""
    if len(player_history) == 0:
        return 0

    if len(player_history) == 1:
        last = move_to_number.get(player_history[-1], 0)
        return last

    second_to_last = move_to_number.get(player_history[-2], 0)
    last = move_to_number.get(player_history[-1], 0)
    return second_to_last * 3 + last

def boss_ai(player_history):
    """Choose the AI's move for this round."""""
    if not player_history:
        from ai_game_logic import easy_ai
        return easy_ai()

    q_table = load_q_table()
    situation = get_situation(player_history)

    if np.random.random() < random_choice:
        return moves[np.random.randint(num_responses)]
    else:
        best_move_index = int(np.argmax(q_table[situation]))
        return moves[best_move_index]


def update_boss_ai(player_history, player_move, result):
    """""""After each round, update the AI's scores based on what happened."""
    if player_move not in move_to_number:
        return

    q_table = load_q_table()
    situation = get_situation(player_history)

    ai_move_index = int(np.argmax(q_table[situation]))

    rewards = {'win': win_reward, 'tie': tie_reward, 'loss': loss_reward}
    reward = rewards.get(result, tie_reward)

    next_situation = get_situation(player_history + [player_move])
    best_future_score = float(np.max(q_table[next_situation]))

    current_score = q_table[situation, ai_move_index]
    q_table[situation, ai_move_index] = (
        current_score + learning_rate * (reward + discount * best_future_score - current_score)
    )

    write_q_table(q_table)
