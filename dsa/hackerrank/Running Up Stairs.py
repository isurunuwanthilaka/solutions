#time limit 2500ms
#https://en.wikipedia.org/wiki/Fibonacci_number

import time
s=time.time()
t=input()
fb=[1,1]
for i in range(22000):
    fb.append(fb[-1]+fb[-2])
for _ in range(t):
    n=input()
    print fb[n]
f=time.time()
print str(f-s)+"ms"
