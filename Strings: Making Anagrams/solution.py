#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = list(a)
    b = list(b)
    ii = 0
    jj = 0
    while ii < len(a):
        jj = 0
        while jj < len(b):
            if a[ii] == b[jj]:
                b.pop(jj)
                a.pop(ii)
                ii -= 1
                break
            jj += 1
        ii += 1
    return (len(a) + len(b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
