def request():
    max=3
    time=5
    timeStamps=[1,2,2,5,7]
    n1=timeStamps[0]
    n2=timeStamps[1]
    n3=n1+n2
    bul=[]

    for i in range(0,7,5):
        if n3<max:
            bool=True
            bul.append(bool)
        else:
            bool=False
            bul.append(bool)

    print(bul)

request()