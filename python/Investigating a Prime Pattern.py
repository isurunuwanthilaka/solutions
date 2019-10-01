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
tot=0
for i in xrange(2,150*10**6,2):
    if all(miller_rabin(n) for n in [i**2+1,i**2+3,i**2+7,i**2+9,i**2+13,i**2+27]):
        if any(miller_rabin(n) for n in [i**2+5,i**2+11,i**2+15,i**2+17,i**2+19,i**2+21,i**2+23,i**2+25]):
            continue
        else:
            tot+=i
print tot
