t=input()
for _ in range(t):
    ar=[1,1]
    n = input()
    n=n%60
    for i in range(n-1):
        ar.append((ar[-1]+ar[-2])%10)
    print ar[-1]
        
