import random

players=int(input("how many players do you guys have?: "))
teamnu=int(input("how many teams do you want?: "))

remainders=players % teamnu
squadnu=players//teamnu
if remainders != 0:
    print("there are going to be {} players left behind" .format(remainders))

squad=list("")

count=0

#acccepting players name
while count < players:
    x=input("enter the name of player {}: " .format(count+1))
    squad.append(x)
    count+=1
    
#randomizing and sharing teams
ctrl=1
con=1
selection=1

while ctrl < players:
    print("team{}-----------\n".format(selection))
    while con <= squadnu:
        print(random.choice(squad))
        con+=1
    selection+=1
    ctrl+=1