import random
def miller_rabin(n, k=5):
    if n==1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

n=input()
a=n-7
while True:
    a-=1
    if miller_rabin(a):
        break
c=n-a
b=c
while True:
    b-=1
    if miller_rabin(b) and miller_rabin(c-b):
        print a,b,c-b
        break
