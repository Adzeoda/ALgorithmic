import time

def countdown(secs):
    while secs:
        mins,secs = divmod(secs, 60)
        timeformat='{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        secs-=1
    print('end')

def countup(secs):
    while secs:
        min

secs=int(input("enter the number of seconds you want to countdown: "))
countdown(secs)
