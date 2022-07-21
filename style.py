from secrets import randbelow


def style(sentence):
    x=len(sentence)
    w=[]

    for i in sentence:
        w+=i

    print(sentence)
    for i in range(x):
        w.pop(x-1)
        print(''.join(w))
        x-=1


style("the quick brown fox jumos over the lazy dog")
