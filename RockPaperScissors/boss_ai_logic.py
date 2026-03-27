"""
Author: Nathaniel Lee
Module: boss_ai_logic
Description: Q-Learning Boss AI for rock-paper-scissors.
"""

import numpy as np
import os
import json

MOVES = ['rock', 'paper', 'scissors']
MOVE_TO_NUMBER = {'rock': 0, 'paper': 1, 'scissors': 2}
SAVE_FILE = "boss_ai_model.json"
LEARNING_RATE = 0.1
DISCOUNT = 0.9
RANDOM_CHANCE = 0.15
WIN_REWARD  =  1.0
TIE_REWARD  =  0.0
LOSS_REWARD = -1.0

NUM_SITUATIONS = 9   
NUM_RESPONSES  = 3   


def load_q_table():
    "Load the AI's learned scores from disk."
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
            q_table = np.array(data["q_table"], dtype=float)
            if q_table.shape == (NUM_SITUATIONS, NUM_RESPONSES):
                return q_table
        except (json.JSONDecodeError, KeyError, ValueError):
            print("[Boss AI] Save file was unreadable. Starting fresh.")

    return np.zeros((NUM_SITUATIONS, NUM_RESPONSES), dtype=float)

def write_q_table(q_table):
    "Save the AI's learned scores to disk so they survive between sessions."
    temp_file = SAVE_FILE + ".tmp"
    with open(temp_file, 'w') as f:
        json.dump({"q_table": q_table.tolist()}, f, indent=2)
    os.replace(temp_file, SAVE_FILE)

def get_situation(player_history):
    "Turn the player's last 2 moves into a single row number for the Q-table."
    if len(player_history) == 0:
        return 0

    if len(player_history) == 1:
        last = MOVE_TO_NUMBER.get(player_history[-1], 0)
        return last

    second_to_last = MOVE_TO_NUMBER.get(player_history[-2], 0)
    last = MOVE_TO_NUMBER.get(player_history[-1], 0)
    return second_to_last * 3 + last

def boss_ai(player_history):
    "Choose the AI's move for this round."
    if not player_history:
        from ai_game_logic import easy_ai
        return easy_ai()

    q_table   = load_q_table()
    situation = get_situation(player_history)

    if np.random.random() < RANDOM_CHANCE:
        return MOVES[np.random.randint(NUM_RESPONSES)]
    else:
        best_move_index = int(np.argmax(q_table[situation]))
        return MOVES[best_move_index]


def update_boss_ai(player_history, player_move, result):
    "After each round, update the AI's scores based on what happened."
    if player_move not in MOVE_TO_NUMBER:
        return

    q_table   = load_q_table()
    situation = get_situation(player_history)

    ai_move_index = int(np.argmax(q_table[situation]))

    rewards = {'win': WIN_REWARD, 'tie': TIE_REWARD, 'loss': LOSS_REWARD}
    reward  = rewards.get(result, TIE_REWARD)

    next_situation    = get_situation(player_history + [player_move])
    best_future_score = float(np.max(q_table[next_situation]))

    current_score = q_table[situation, ai_move_index]
    q_table[situation, ai_move_index] = (
        current_score
        + LEARNING_RATE * (reward + DISCOUNT * best_future_score - current_score)
    )

    write_q_table(q_table)