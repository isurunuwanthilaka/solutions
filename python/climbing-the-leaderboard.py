#!/bin/python

import sys


n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
alice.reverse()
scores=list(set(scores))
scores.sort()
scores.reverse()
arr=[]
a=0
b=0
k=1
while len(alice) and len(scores):
    a=alice[0]
    b=scores[0]
    if a>=b:
        arr.append(k)
        del alice[0]
    else:
        k+=1
        del scores[0]
s=alice[:]
s=list(set(s))
s.sort()
s.reverse()
for i in s:
    for j in range(alice.count(i)):
        arr.append(k)
    k+=1
arr.reverse()
for i in arr:
    print i
