#reference - hackerrank 
'''
(https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)
'''

#dynamic programming

#!/bin/python3
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
'''
def jumpingOnClouds(c):
    n = len(c)
    if n==1:
        return 0
    if n == 2:
        if c[0]==c[1]:
            return 1
        else:
            return jumpingOnClouds(c[1:])
    if c[1]==1:
        return 1+jumpingOnClouds(c[2:])
    if c[2]==1:
        return 1+ jumpingOnClouds(c[1:])
    return min(1+jumpingOnClouds(c[1:]), 1+jumpingOnClouds(c[2:]))
'''
global d
d = {}
def jumpingOnClouds(c):
    n = len(c)
    if n in d:
        return d[n]
    if n==1:
        return 0
    if n == 2:
        if c[0]==c[1]:
            return 1
        else:
            d[n] = jumpingOnClouds(c[1:])
            return d[n]
    if c[1]==1:
        d[n] = 1+jumpingOnClouds(c[2:])
        return d[n]
    if c[2]==1:
        d[n] = 1+ jumpingOnClouds(c[1:])
        return d[n]
    tmp1 = 1+jumpingOnClouds(c[1:])
    tmp2 = 1+jumpingOnClouds(c[2:])
    d[n] = min(tmp1,tmp2)
    return d[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

