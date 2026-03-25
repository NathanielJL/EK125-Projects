'''
Author: Suvanjal Dhungana 
Module: Tournament Sytem 

def playseries(bestof):
        playerScore = 0
        aiScore=0
        roundNumber = 1
        roundsNeededToWin = (format //2 ) + 1

        print("Starting best of ",+format+"Series")

        while playerScore < roundsNeededToWin and aiScore < roundsNeededToWin :
            print("Round ",roundNumber)
            playerMove = getPlayermove()
            aiMove = getAImove()

            roundResult = determineRounderWinner(playerMove, aiMove)

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
    while True:
        bestof = startTournament()
        playseries(bestof)

        another_series = input("Do you want to play another series? (y/n): ").lower()
        if another_series != "y":
            break

    print("Thank you for playing!")
