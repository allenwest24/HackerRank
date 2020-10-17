#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    ret = []
    for ii in range(3):
        if a[ii] > b[ii]:
            alice += 1
        elif b[ii] > a[ii]:
            bob += 1
    ret.append(alice)
    ret.append(bob)
    return ret
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
