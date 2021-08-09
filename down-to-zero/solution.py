#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

tbl = {}



def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False 
    return True

primes = [2,3,5,7]
prime_limit = 1000

i = 8
while primes[-1]*2 < (10**6 + 1):
    print(f"last prime: {primes[-1]} primes[-1]*2 = {primes[-1]*2} total primes: {len(primes)}")
    if is_prime(i):
        primes.append(i)
    i += 1

print(f"Needed primes: {len(primes)} {primes}")

def incset(m, k):
    if k in m:
        m[k] += 1
    else:
        m[k] = 1
    

def factorize(n): 
    factors = {}
    
    for f in primes:        
        while n % f == 0:
            incset(factors, f)
            n = n // f        
        if n == 1:
            return factors
    if n > 1:
        incset(factors, n)    
    return factors


for i in range(3, 10**6 + 1):
    if i % 1000 == 0:
        print(f"Factorized {i} numbers")
    factorize(i)

print(f"is_prime(7793): {is_prime(7793)}")
assert False, "Stop"


def max(a, b):
    if a > b:
        return a 
    return b

def min(a, b):
    if a < b:
        return a
    return b

# 20
# 2 * 2 = 4     3 * 2 = 6
# 2 * 3 = 6     
# 2 * 4 = 8     3 * 3 = 9
# 2 * 5 = 10   
# 2 * 6 = 12    3 * 4 = 12
# 2 * 7 = 14    3 * 5 = 15
# 2 * 8 = 16    3 * 6 = 18
# 2 * 9 = 18    
# 2 * 10 = 20




for i in range(2, 10**6):
    j = 2    
    while (i * j) < 10**6:
        print(f"I: {i} j: {j}")
        p = i * j     
        if p in tbl:
            tbl[p] = min(tbl[p], max(i, j))
        else:
            tbl[p] = max(i, j)
        j += 1
    

for i in range(int(math.sqrt(10**6)), int(math.sqrt(10**6)) - 100, -1):
    if i in tbl:
        print(f"[{i}]={tbl[i]}")

def downToZero(n):
    steps = 0
    while n != 0:        
        if n in tbl:            
            n = tbl[n]
        else:
            n -= 1
        steps +=1
    # Write your code here
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
