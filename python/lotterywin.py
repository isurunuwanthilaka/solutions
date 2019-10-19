
import math
import os
import random
import re
import sys
import itertools

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

# Complete the winningLotteryTicket function below.
def winningLotteryTicket(tickets):
    c=0
    tickets_u = set(tickets)
    print(tickets_u)
    if len(tickets_u)>=2:
        for i in itertools.combinations(tickets_u,2):
            if len(i[0]+i[1])>=10:
                if len(set(list(i[0]+i[1])))==10:
                    c+=tickets.count(i[0])*tickets.count(i[1])
        for k in tickets_u:
            if len(k)==10:
                if tickets.count(k)>=2:
                    print(tickets.count(k))
                    c+= nCr(tickets.count(k),2)
    else:
        for j in tickets_u:
            if len(j)==10:
                if tickets.count(j)>=2:  
                    c+= nCr(tickets.count(j),2)
    return int(c)


if __name__ == '__main__':

    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        temp =list(set(list(tickets_item)))
        temp.sort()
        s=''
        tickets_item = s.join(temp)
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)
    print(result)
