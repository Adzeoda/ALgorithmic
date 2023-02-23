import random

vars=["r","p","s"]
yourscore=0
opscore=0
count=1

def win(yourvar,opsvar):
    global count
    global yourscore
    print("you played {} your opponent played {} you win game {}".format(yourvar,opsvar,count))
    yourscore+=1
    print("the scores is {} - {}" .format(yourscore,opscore))
    if yourscore> opscore:
        print("In your favor")
    elif yourscore<opscore:
        print("in opponents favour")
    count+=1

def lose(yourvar,opsvar):
    global count
    global opscore
    print("you played {} your opponent played {} you lose game {}".format(yourvar,opsvar,count))
    opscore+=1
    print("the scores is {} - {}" .format(yourscore,opscore))
    if yourscore> opscore:
        print("In your favor")
    elif yourscore<opscore:
        print("in opponents favour")
    count+=1

def draw(yourvar):
    global count
    print("you both played {} you draw".format(yourvar))
    print("the scores is still {} - {}" .format(yourscore,opscore))
    if yourscore> opscore:
        print("In your favor")
    elif yourscore<opscore:
        print("in opponents favour")
    count+=1

for i in range(5):
    print("select 'R' for 'rock', 'P' for 'paper', or 'S' for 'scissors'")
    yourvar=input(": ")
    yourvar=yourvar.lower()
    opsvar=random.choice(vars)
    
    if yourvar=="r":
        if opsvar=="r":
            draw("r")
        elif opsvar=="p":
            lose("r","p")
        elif opsvar=="s":
            win("r","s")
        else:
            print("invalid respose")
    
    elif yourvar=="p":
        if opsvar=="p":
            draw("p") 
        elif opsvar=="s":
            lose("p","s")
        elif opsvar=="r":
            win("p","s")
        else:
            print("invalid response")

    elif yourvar=="s":
        if opsvar=="s":
            draw(yourvar)
        elif opsvar=="r":
            lose(yourvar,opsvar)
        elif opsvar=="p":
            win(yourvar,opsvar)

    else:
        print("INVALID RESPONSE!")