def mutliplier(number):
    for i in range(1,24):
        answer = i*number
        print(number, "x ", i , "=", answer)

# mutliplier(12)

def mutlitable():
    for i in range(1,13):
        for j in range(1,13):
            print(i, "x", j ,"=" ,i*j)
        print("-------------")


mutlitable()