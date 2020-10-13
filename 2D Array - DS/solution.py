#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    best = 0
    curr = 0
    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr[0]) - 1):
            curr = arr[y][x] + arr[y-1][x-1] + arr[y-1][x] + arr[y-1][x+1] + arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1]
            if curr > best or (y == 1 and x == 1):
                best = curr
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
