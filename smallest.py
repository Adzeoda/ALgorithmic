def solution(a,n):
    b=[]
    n.sort()
    a.sort()
    for i in range(n[0],n[1]):
        if i in a:
            j=i
            b.append(j)
        b.sort()
        print(b[0])

        if i not in a:
            print("none")
        
solution([2,3,4,5,6,7,8],[4,2])