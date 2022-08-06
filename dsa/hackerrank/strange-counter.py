import math
import os
import random
import re
import sys

def strangeCounter(t):

    if t>=4: 
        m=2
        while True:
            tforward=4+6*(2**(m-1)-1)
            if tforward>t:
                a=4+6*(2**(m-2)-1)
                b=3*(2**(m-1))
                result=a+b-t
                break
            m+=1
    else:
        result=4-t
    
    return result

t = int(input())
result = strangeCounter(t)
print(result)
