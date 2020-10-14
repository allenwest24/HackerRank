#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    ii = 0
    while ii < len(c):
        if ii == len(c) - 1:
            break
        if ii == len(c) - 2:
            ii += 1
        elif ii == len(c) - 3:
            ii += 2
        elif c[ii + 2]:
            ii += 1
        else:
            ii += 2
        jumps += 1
    return jumps
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
