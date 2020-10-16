#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    print(arr)
    ii = k - 1
    low = 0
    while ii < len(arr):
        print(low)
        if ii == k - 1 or arr[ii] - arr[ii - k] < low:
            low = arr[ii] - arr[ii - k]
        ii += 1
    return low
         


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
