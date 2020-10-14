#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# Array = a
# Rotations left = d
def rotLeft(a, d):
    while d > 0:
        tmp = a.pop(0)
        a.append(tmp)
        d -= 1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
