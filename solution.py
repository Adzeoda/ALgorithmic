from operator import truediv


def solution():
    a=[]
    b=a
    n=int(input('size of array: '))
    print("enter the elements of a: ")

    for i in range(n):
        x=int(input("the element {}: ".format(i)))
        a.append(x)

    print(a)
    
    for j in a:
        if i==0:
            j=a[0]+a[1]
            b.append(j)
        else:
            j=a[j-1]-a[j]+a[j+1]
            b.replace(j)
    return b




def Palindrome(String):
    inp = String.lower()

    old=""
    count=0
    i=inp[0]
    while count<len(inp):
        if i==inp[count]:
            old+=i
            i=inp[count]
        count+=1

    print(old)

    output=inp.translate({ord("N"):None})

    # inp.purge(vim)

    print(output)

    # reverse = inp[::-1]

    # if (reverse == inp):
    #     print("palindrome")
    # else:
    #     print("not palindrome")

Palindrome("aaaacock")

#find list remove