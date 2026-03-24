def initialize_stats():
    '''
    Creates and returns a clean statistics dictionary with all 
    values set to zero.
    
    returns: 
        stats (dict): A dictionary tracking wins, losses, ties, 
                      streaks, and ai throws for each throw type.
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

    Args:
        stats (dict): The current stats dictionary to update.
        player_throw (str): The players chosen throw (rock, paper, 
                            scissors).
        ai_throw (str): The ai's chosen throw (rock, paper, 
                        scissors).
        result (str): The result of the game from players POV (win, 
                      loss, tie).
    
    Returns:
        stats (dict): The updated stats dictionary.
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