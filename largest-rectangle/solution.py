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


    
def two_pointers(h):
    l = 0
    r = len(h) -1 
    res = float('-inf')
    while l < r:
        res = max(res, min(h[l:r+1]) * (r - l + 1))
        if h[l+1] > h[l]:
            l += 1
        else:
            r -= 1
    return res

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
    return two_pointers(h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
