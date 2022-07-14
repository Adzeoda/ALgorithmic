noRooms=int(input("enter the number of rooms in the house: "))
roomPopulation=list("")

count=1
housePop=0

while count<=noRooms:
    print("enter the number of occupants in room{}: ".format(count))
    x=int(input(": "))
    roomPopulation.append(x)
    housePop+=x
    count+=1
print("there are {} people living here".format(housePop))

#billing
bill=float(input("enter the bill amount in floating digits eg'100.00: "))
quota=bill/housePop
print("the quota is {}" .format(quota))

count2=0
while count2<=len(roomPopulation)-1:
    print("room {} pays {}GHc" .format(count2+1,roomPopulation[count2]*quota))
    count2+=1