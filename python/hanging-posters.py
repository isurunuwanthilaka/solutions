#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

def solve(h, wallPoints, lengths):
    # Write your code here
    ls=[]
    for i in range(len(wallPoints)):
        ls.append(math.ceil(wallPoints[i]-lengths[i]/4.0-h))
    r= max(ls)
    if r<0:
        return 0
    else:
        return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    fptr.write(str(answer) + '\n')

    fptr.close()
