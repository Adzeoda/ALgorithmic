import random

count=0

num=random.randint(1,100)

guess=int(input("guess the number between 1 and hundred: "))


while guess!=num:
    # guess=input(: )
    if guess>num:
        print("wrong answer go again hint go higher: ")
        guess=input(": ")
    elif guess<num:
        print("wrong answer go again hint go lower: ")
        guess=input(": ")