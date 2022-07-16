def fibunaaciNth(nth):
    n1=0
    n2=1
    n3=n1+n2

    while n3<nth:
        print(n3)
        n1=n2
        n2=n3
        n3=n1+n2

def fibunacciN(n):
    n1=0
    n2=1
    n3=n1+n2
    count=0

    while count<n:
        print(n3)
        n1=n2
        n2=n3
        n3=n1+n2
        count+=1

fibunaaciNth(100)
fibunacciN(100)