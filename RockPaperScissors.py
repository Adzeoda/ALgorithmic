import random

obj = ["rock", "paper", "scissors"]

nuGames = int(input("how many rounds do you want to play?: "))

player = int(input("enter 1 for rock, 2 for paper or 3 for scissors: "))

# scores
count = 1
comScore = 0
yourScore = 0

while count < nuGames:
    while player not in (1, 2, 3):
        print("sorry, invalid answer input 1 for rock, 2 for paper or 3 for scissors")
        player = int(input(": "))
        player -= 1
        
        comPlayed = random.randint(0, 2)


        if comPlayed == player:
            print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
            count += 1

        if comPlayed == 0:
            if player == 1:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                yourScore += 1
                print("you win, you have{} points, computer has{}, points".format(yourScore, comScore))
            elif player == 2:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                comScore += 1
                print("you lose, you have{} points, computer has{}, points".format(yourScore, comScore))

        if comPlayed == 1:
            if player == 0:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                comScore += 1
                print("you lose, you have{} points, computer has{}, points".format(yourScore, comScore))
            elif player == 2:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                yourScore += 1
                print("you win, you have{} points, computer has{}, points".format(yourScore, comScore))

        if comPlayed == 2:
            if player == 0:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                yourScore += 1
                print("you win, you have{} points, computer has{}, points".format(yourScore, comScore))
            elif player == 1:
                print("you played{}, computer played{}".format(obj[player], obj[comPlayed]))
                comScore += 1
                print("you lose, you have{} points, computer has{}, points".format(yourScore, comScore))

    print("you've played{} games, you've won{} games and computer has won{}, {}games more".format(count, yourScore,comScore,count - nuGames))
