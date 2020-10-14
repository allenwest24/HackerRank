#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total = 0
    if len(s) < n:
        temp_lim = len(s)
    else:
        temp_lim = n
    for ii in range(temp_lim):
        if s[ii] == 'a':
            total += 1
    if n > len(s):
        mult = math.floor(n / len(s))
        total *= mult
        for jj in range(n % len(s)):
            if s[jj] == 'a':
                total += 1
            
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
