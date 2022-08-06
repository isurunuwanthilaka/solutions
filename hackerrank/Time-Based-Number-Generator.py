t =int(input()) ## get the input
d=3
while True:    
    if t-d>0:
        t=t-d
        d=d*2
    else:
        print(d-t+1)
        break

