import random

gameObjs=["rock","paper","scissors"]

numberGames=int(input("how many games do you want to play?: "))
count=0

while count<numberGames:
    games=input("enter 1 for rock, 2 for paper, 3 for scissors: ")
    if games <1 and games>3:
        print("ENTER A NUMBER FROM 1 TO 3")
        games=input(" :")
