import random

yourPoints=0
comPoints=0

def authentication(x,y,yourPoints,comPoints):
    if x==1:
        if y==1:
          print("you draw you both played rock")
        if y==2:
            comPoints+=1
            print("you played rock and computer played paper, you lost you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))
        if y==3:
            yourPoints=+1
            print("you played rock and computer played scissors, you won you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))
    if x==2:
        if y==1:
            yourPoints+=1
            print("you played paper and computer played rock, you won you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))
        if y==1:
            print("you both played paper you have{} and computer has {} points".format(yourPoints,comPoints))
        if y==3:
            comPoints+=1
            print("you played paper and computer played scissors, you lost you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))

    if x==3:
        if y==1:
            comPoints+=1
            print("you played scissors and computer played rock, you lost you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))
        if y==2:
            yourPoints+=1
            print("you played scissors and computer played paper, you lost you have {} points and yiur opponent has {} points ".format(comPoints,yourPoints))
        if y==2:
            print("you both played paper you have{} and computer has {} points".format(yourPoints,comPoints))


game=("rock","paper","scissors")

nu=input("enter the number of games you want to play: ")
x=input("1 for rock, 2 for paper and 3 for scissors: ")

y=random.randint(1,3)

for i in range(nu):
    if x<1 or x>3:
        print("wrong input enter 1 for rock 2 for paper or 3 for scissors: ")

    elif x==1:
        y=random.randint(1,3)
        

