#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def iter_walk2(tree, q):
    stack = []
    res = []
    node = (1, 1)
    while node[0] != -1 or len(stack) > 0:
        
        if node[0] != -1:
            idx = node[0] - 1
            if node[1] % q == 0:
                tree[idx][0], tree[idx][1] = tree[idx][1], tree[idx][0]
            stack.append(node)
            node = (tree[node[0] - 1][0], node[1]+1)
        else:
            node = stack.pop()
            res.append(node[0])
            node = (tree[node[0] - 1][1], node[1]+1)
    return res

def iter_walk(tree, n):
    visited = set([-1])
    swapped = set()
    path = [(1, 1)]
    res = []
    while len(path) > 0:        
        idx, depth = path.pop()                
        node = tree[idx - 1]
                
        if depth % n == 0 and idx not in swapped:            
            swapped.add(idx)
            node[0], node[1] = node[1], node[0]
            
        if node[0] not in visited:            
            path.append((idx, depth))
            path.append((node[0], depth + 1))
            continue
        
        res.append(idx)
        visited.add(idx)

        if node[1] not in visited:
            path.append((node[1], depth + 1))
    
    return res


def swapNodes(indexes, queries):
    # Write your code here
    res = []

    print(iter_walk2(indexes, 1000))
    for q in queries: res.append(iter_walk2(indexes, q))
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
