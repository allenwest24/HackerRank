#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    total = 0
    for ii in range(len(arr)):
        curr = arr[ii]
        if curr > ii + 1:
            to_swap = arr.index(ii + 1, ii + 1, len(arr))
            tmp = arr[to_swap]
            arr[to_swap] = curr
            curr = tmp
            total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
