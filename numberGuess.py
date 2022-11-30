import random

number=random.randint(0,100)
print(number)
guess=int(input("guess the number: "))
count=1

if guess==number:
    print("congratulations you guessed the right number")

while guess!= number:
    if guess>number:
        guess=int(input("wrong guess, you have made {} attempt(s), guess lower: ".format(count)))
    elif guess<number:
        guess=int(input("wrong guess, you have made {} attempt(s), guess  higher: ".format(count)))
    count+=1

if guess==number:
    print("congratulations you guessed the right number in your {} attempt". format(count))