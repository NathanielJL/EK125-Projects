"""
Author: Nathaniel Lee, Kacper Wajler, Suvanjal Dhungana
Module: main
Description: This module contains the main function that runs the Rock Paper Scissors game. 
It initializes the game, handles user input, and manages the game loop until the user decides to quit.
"""

import time

def display_welcome():
    "Display welcome banner and menu."
    print("Starting in 3 seconds...")
    time.sleep(3)
    print("=" * 50)
    print("Welcome to Rock Paper Scissors Tournament!")
    print("=" * 50)
    print("")

def get_game_mode():
    "Get user's preferred game mode."
    while True:
        mode = input("Do you want to play in tournament mode? (yes/no): ").lower().strip()
        if mode in ['yes', 'no']:
            return 'tournament' if mode == 'yes' else 'single'
        print("Invalid input. Please enter 'yes' or 'no'.")

def get_tournament_format():
    "Get tournament format if tournament mode is selected."
    valid_formats = ['best-of-3', 'best-of-5', 'best-of-7']
    while True:
        tournament = input("Select tournament format (best-of-3, best-of-5, best-of-7): ").lower().strip()
        if tournament in valid_formats:
            return tournament
        print(f"Invalid format. Please choose from: {valid_formats}")


def get_ai_difficulty():
    "Get AI difficulty level."
    valid_difficulties = ['easy', 'medium', 'hard', 'boss']
    while True:
        difficulty = input("Choose AI difficulty (easy, medium, hard, boss): ").lower().strip()
        if difficulty in valid_difficulties:
            return difficulty
        print(f"Invalid difficulty. Please choose from: {valid_difficulties}")


def main():
    "Main entry point for the game."
    
    display_welcome()
    game_mode = get_game_mode()
    ai_difficulty = get_ai_difficulty()
    
    try:
        if game_mode == 'tournament':
            tournament_format = get_tournament_format()
            from tournament_logic import run_tournament
            run_tournament(tournament_format, ai_difficulty)
        else:
            from ai_game_logic import play_single_game
            play_single_game(ai_difficulty)
            
    except ValueError:
        print(f"\nERROR")
    
    print("\n" + "=" * 50)
    print("Thanks for playing! Goodbye!")
    print("=" * 50)

if __name__ == "__main__":
    main()