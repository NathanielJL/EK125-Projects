ROCK PAPER SCISSORS
Team: Kacper, Nathaniel, Suvanjal

HOW TO RUN THE GAME:

1. Open PyCharm and load the EK125-Projects folder
2. Open main.py
3. Click the green Run button in the top right corner
4. Follow the on-screen prompts to select a game mode, AI difficulty,
   and tournament format

TEAM CONTRIBUTIONS:

Nathaniel — ai_game_logic.py, boss_ai_logic.py
    Handles core game logic and AI opponents. This includes basic
    rock-paper-scissors rules, random AI, pattern AI, counter AI,
    boss AI, and player input validation.

Suvanjal — tournament_logic.py
    Handles the tournament system. This includes best-of-3, best-of-5,
    and best-of-7 formats, round tracking, match and series winner
    determination, and the ability to play multiple series.

Kacper — statistics.py
    Handles all statistics tracking and analysis. This includes
    win/loss/tie tracking per throw type, win percentage calculation,
    current and longest win streaks, most common player and AI throws,
    and the end-of-series statistics report.

FILE STRUCTURE:

main.py              — Main entry point, connects all modules
ai_game_logic.py     — Core game logic and AI strategies (Nathaniel)
boss_ai_logic.py     — Boss AI logic (Nathaniel)
tournament_logic.py  — Tournament system (Suvanjal)
statistics.py        — Statistics tracking and display (Kacper)

KNOWN ISSUES:

- No known bugs at time of submission
- Game runs in terminal only

FUTURE ENHANCEMENT IDEAS:

- Add a leaderboard that saves scores to a .txt file
- Add more AI difficulty levels
