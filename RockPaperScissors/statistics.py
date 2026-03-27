"""
Author: Kacper Wajler

Student C: Statistics & Analysis
- Track win/loss/tie for each throw type
- Calculate win percentage
- Track current streak (wins/losses)
- Longest win streak
- Most common player choice
- Most common AI choice
- Head-to-head results by throw type
"""
def initialize_stats():
    '''
    Creates and returns a clean statistics dictionary with all 
    values set to zero.
    '''
    stats = {
        'total_games': 0,
        'current_streak': 0,
        'longest_streak': 0,

        'ai_total': {
            'rock': 0,
            'paper': 0,
            'scissors': 0
        },

        'rock': {
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'ai_threw': {'rock': 0, 'paper': 0, 'scissors': 0}
        },

        'paper': {
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'ai_threw': {'rock': 0, 'paper': 0, 'scissors': 0}
        },

        'scissors': {
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'ai_threw': {'rock': 0, 'paper': 0, 'scissors': 0} 
        }
    }
    return stats

def update_stats(stats, player_throw, ai_throw, result):
    '''
    Updates the stats dictionary after each round of the game.
    '''
    stats['total_games'] += 1

    if result == 'win':
        stats[player_throw]['wins'] += 1
    elif result == 'loss':
        stats[player_throw]['losses'] += 1
    elif result == 'tie':
        stats[player_throw]['ties'] += 1
    
    stats[player_throw]['ai_threw'][ai_throw] += 1
    stats['ai_total'][ai_throw] += 1

    if result == 'win':
        stats['current_streak'] += 1
        if stats['current_streak'] > stats['longest_streak']:
            stats['longest_streak'] = stats['current_streak']
    elif result == 'loss' or result == 'tie':
        stats['current_streak'] = 0
    
    return stats

def calculate_win_percentage(stats):
    '''
    Calculates the player's win percentage from the stats dictionary.
    '''
    if stats['total_games'] == 0:
        return 0.0

    total_wins = stats['rock']['wins'] + stats['paper']['wins'] + stats['scissors']['wins']

    win_percentage = total_wins / stats['total_games'] * 100

    return win_percentage

def get_most_common(stats):
    '''
    Determines the most common throw for both the player and the AI.
    '''
    player_throws = {
        'rock': stats['rock']['wins'] + stats['rock']['losses'] + stats['rock']['ties'],
        'paper': stats['paper']['wins'] + stats['paper']['losses'] + stats['paper']['ties'],
        'scissors': stats['scissors']['wins'] + stats['scissors']['losses'] + stats['scissors']['ties']
    }

    most_common_player = max(player_throws, key=player_throws.get)
    most_common_ai = max(stats['ai_total'], key=stats['ai_total'].get)

    return most_common_player, most_common_ai

def display_stats(stats):
    '''
    Displays a formatted end of series statistics report.
    '''
    win_pct = calculate_win_percentage(stats)
    most_common_player, most_common_ai = get_most_common(stats)
    total_wins = stats['rock']['wins'] + stats['paper']['wins'] + stats['scissors']['wins']
    total_losses = stats['rock']['losses'] + stats['paper']['losses'] + stats['scissors']['losses']
    total_ties = stats['rock']['ties'] + stats['paper']['ties'] + stats['scissors']['ties']

    print("\n" + "=" * 50)
    print("      END OF SERIES STATISTICS REPORT")
    print("=" * 50)

    print(f"\nTotal Games Played : {stats['total_games']}")
    print(f"Wins               : {total_wins}")
    print(f"Losses             : {total_losses}")
    print(f"Ties               : {total_ties}")
    print(f"Win Percentage     : {win_pct:.1f}%")
    print(f"Longest Win Streak : {stats['longest_streak']}")
    print(f"Current Streak     : {stats['current_streak']}")

    print(f"\nMost Common Player Throw : {most_common_player.capitalize()}")
    print(f"Most Common AI Throw     : {most_common_ai.capitalize()}")

    print("\n--- Win / Loss / Tie by Throw ---")
    for throw in ['rock', 'paper', 'scissors']:
        w = stats[throw]['wins']
        l = stats[throw]['losses']
        t = stats[throw]['ties']
        print(f"  {throw.capitalize():8s}: {w}W / {l}L / {t}T")

    print("\n--- Head-to-Head (Your Throw vs AI Throw) ---")
    for throw in ['rock', 'paper', 'scissors']:
        ai_threw = stats[throw]['ai_threw']
        print(f"  When you threw {throw.capitalize()}:")
        for ai_throw, count in ai_threw.items():
            print(f"    vs AI {ai_throw.capitalize():8s}: {count} time(s)")

    print("=" * 50)
