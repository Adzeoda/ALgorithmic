def alt():
    a=[]
    s="aaaaa"
    t="bbb"
    for i in s:
        a.append(i)
        for j in t:
            if j in t:
                a.append(j)
                break
    print(''.join(a))


alt()