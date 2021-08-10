#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

#  1  2  3  4  5 
#  0  1  2  3  4 (-1)
# -1  0  1  2  3 (-2)
# -2 -1  0  1  2 (-3)
# -3 -2 -1  0  1 (-4)
# -4 -3 -2 -1  0 (-5)

# The idea behind the algorithm:
# We keep an increasing stack of heights and the index where
# we encountered that height. When next hight is lower than
# latest in the stack, we compare which squares the current index
# complets and save max.
# One we iterated over everything, we check non-completed squares too.
def use_mem(h):
    path = [(h[0], 0)]
    mh = float('-inf')

    for i in range(1, len(h)):
        j = len(path) - 1
        while j >= 0 and path[j][0] > h[i]:
            height, start = path[j]
            mh = max(mh, height * (i - start))
            path[j] = (h[i], start)
            j -= 1        
        if h[i] > path[-1][0]:
            path.append((h[i], i))
        
    while len(path) > 0:
        height, start = path.pop()
        mh = max(mh, height * (i - start + 1))

    return mh

def brute_force(h):
    res = float('-inf')
    hs = set(h)    
    for i in hs:
        ml = 0
        for j in h:
            if j - i < 0:
                res = max(res, ml * i)
                ml = 0
            else:
                ml += 1
        res = max(res, ml * i)
    return res

def largestRectangle(h):
    return use_mem(h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
