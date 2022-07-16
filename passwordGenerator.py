import random
def passwordGenerator(lenght):
    password=[]
    # holder=[]
    capitals=tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numerals=tuple("1234567890")
    symbols=tuple("!@#$%^&*()?.")
    smalls=("abcdefghijklmnopqrstuvwxyz")
    for i in range(lenght):
        password+=random.choice(capitals)
        password+=random.choice(numerals)
        password+=random.choice(symbols)
        password+=random.choice(smalls)
    holder.append(password)
    
    holder=random.shuffle(holder)

    print(''.join(holder))

passwordGenerator(10)