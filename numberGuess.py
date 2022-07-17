import random

count=0

num=random.randint(1,100)

guess=int(input("guess the number between 1 and hundred: "))

for i in range(10):
    if num==guess:
        print("correct you got it right in attempt no {}" .format(count))
        break
    elif num<guess:
        print("wrong answer, guess higher\n you have{} attempts left: ".format(count+1))
    else:
        print("wrong answer, guess higher\n you have {} attempts left".format(count+1))
    count+=1    