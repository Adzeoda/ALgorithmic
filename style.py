from secrets import randbelow


def style(sentence):
    x=len(sentence)
    w=[]

    for i in sentence:
        w+=i

    print(sentence)
    for i in range(x):
        w.pop(x-1)
        # w.translate([0]," ")
        print(''.join(w))
        x-=1


sentence=input("enter the sentence you want me to slant: ")
style(sentence)