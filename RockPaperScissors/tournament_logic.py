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

def playseries(bestof):
        '''Enables user to play a round, uses function from ai logic module, displays current round and score, 
        ultimately displaying the winner of the series '''
        playerScore = 0
        aiScore=0
        roundNumber = 1
        roundsNeededToWin = (format //2 ) + 1

        print("Starting best of ",+ format +"Series")

        while playerScore < roundsNeededToWin and aiScore < roundsNeededToWin :
            print("Round ",roundNumber)
            playerMove = get_player_move()
            aiMove = get_ai_move()

            roundResult = determine_winner(playerMove, aiMove)

            if roundResult == "Player":
                playerScore = playerScore + 1
                print("Player wins this round!")
            elif roundResult == "AI":
                aiScore = aiScore + 1
                print("AI wins this round!")
            else:
                print("This round is a tie!")

            print("Score: Player", playerScore, "AI - ", aiScore)
            roundNumber = roundNumber + 1

        if playerScore > aiScore:
            print("Player wins this series!")
        else:
            print("AI wins this series!")

def tournamentLoop():
        '''Enables the function above, using function from ai logic containing user format choice
        and asks user again to play another series'''
    while True:
        bestof = get_tournament_format()
        playseries(bestof)

        another_series = input("Do you want to play another series? (y/n): ").lower()
        if another_series != "y":
            break

    print("Thank you for playing!")
