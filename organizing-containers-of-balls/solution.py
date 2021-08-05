#!/bin/python3

import math
import os
import random
import re
import sys

# 0 2 1
# 1 1 1
# 2 0 0



#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def inc_set(m, k):
    if not k in m:
        m[k] = 1
    else:
        m[k] += 1

def organizingContainers(ctrs):
    b_map = {}
    c_map = {}
    l = len(ctrs)
    for i in range(l):
        c = 0
        b = 0
        for j in range(l):
            c += ctrs[i][j]
            b += ctrs[j][i]
        inc_set(c_map, c)
        inc_set(b_map, b)
    if not set(c_map) == set(b_map):
        return "Impossible"
    for k in set(c_map):
        if c_map[k] != b_map[k]:
            return "Impossible"
    return "Possible"
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
