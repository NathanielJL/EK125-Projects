'''
Author: Suvanjal Dhungana 
Module: tournament_logic
Description: Tracks round scores, determines winner and ability to play again

Student B: Tournament System
- Best-of-3, best-of-5, best-of-7 formats
- Round tracking (display current round, scores)
- Match winner determination
- Series winner determination
- Ability to play multiple series

'''
from statistics import update_stats
from ai_game_logic import get_player_move, get_ai_move, determine_winner
from main import get_tournament_format #function used from ai_game_logic

def playseries(tournament, ai_difficulty, stats):
        '''Enables user to play a round, uses function from ai logic module, displays current round and score, 
        ultimately displaying the winner of the series '''
        bestof = int(tournament.split("-")[-1])
        
        playerScore = 0
        aiScore=0
        roundNumber = 1
        roundsNeededToWin = (bestof // 2 ) + 1

        print(f"Starting {tournament} Series")
        
        while playerScore < roundsNeededToWin and aiScore < roundsNeededToWin :
            print("Round ",roundNumber)
                
            playerMove = get_player_move() #function used from ai_game_logic
            aiMove = get_ai_move(ai_difficulty) #function used from ai_game_logic

            roundResult = determine_winner(playerMove, aiMove) #function used from ai_game_logic

            #update scores
            if roundResult == "win":
                playerScore = playerScore + 1
                print("Player wins this round!")
                result ='win'
            elif roundResult == "loss":
                aiScore = aiScore + 1
                print("AI wins this round!")
                result ='loss'
            else:
                print("This round is a tie!")
                result ='tie'

            # update stats here

            stats = update_stats(stats, playerMove, aiMove, result)
            print("Score: Player", playerScore, "AI - ", aiScore)
            roundNumber = roundNumber + 1

        if playerScore > aiScore:
            print("Player wins this series!")
        else:
            print("AI wins this series!")
        return stats


def tournamentLoop(tournament, ai_difficulty, stats):
    '''Enables the function above, using function from ai logic containing user format choice
    and asks user again to play another series'''
    while True:
        stats = playseries(tournament, ai_difficulty,stats)

        another_series = input("Do you want to play another series? (yes/no): ").lower()
        if another_series != "yes":
            break
    
    print("Thank you for playing!")
    return stats

#test cases 
def test_playseries():
    player_moves = test_get_player_move()
    ai_moves = test_get_ai_move('easy')
    stats = {}

    # Replace the original functions with test versions inside playseries
    def get_player_move():
        return next(player_moves)

    def get_ai_move(ai_difficulty):
        return next(ai_moves)

    def determine_winner(player_move, ai_move):
        return test_determine_winner(player_move, ai_move)

    def update_stats(stats, player_move, ai_move, result):
        return test_update_stats(stats, player_move, ai_move, result)

        #running a test with own numbers 
    bestof = 3
    playerScore = 0
    aiScore = 0
    roundNumber = 1
    roundsNeededToWin = (bestof // 2) + 1

    print(f"Starting best-of-{bestof} Series")

    while playerScore < roundsNeededToWin and aiScore < roundsNeededToWin:
        print("Round", roundNumber)

        playerMove = get_player_move()
        aiMove = get_ai_move('easy')

        roundResult = determine_winner(playerMove, aiMove)

        if roundResult == "win":
            playerScore += 1
            print("Player wins this round!")
            result = 'win'
        elif roundResult == "loss":
            aiScore += 1
            print("AI wins this round!")
            result = 'loss'
        else:
            print("This round is a tie!")
            result = 'tie'

        stats = update_stats(stats, playerMove, aiMove, result)
        print(f"Score: Player {playerScore} - AI {aiScore}")
        roundNumber += 1

    if playerScore > aiScore:
        print("Player wins this series!")
    else:
        print("AI wins this series!")
    return stats

if __name__ = '__main__'

