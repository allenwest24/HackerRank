#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for ii in range(len(a)):
        for jj in range(len(a) - 1):
            if a[jj] > a[jj + 1]:
                tmp = a[jj]
                a[jj] = a[jj + 1]
                a[jj + 1] = tmp
                swaps += 1
    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[len(a) - 1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
