def solution(a,n):
    b=[]
    for i in range(n):
        if i==1:
            j=a[0]+a[1]
            b.append(j)
        else:
            j=a[i-1]-a[i]+a[i+1]
            b.append(j)
    print(b)

solution([1,2,3,4,5],5)