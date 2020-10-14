#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    br = 0
    for ii in range(len(q)):
        if (ii < len(q) - 1 and q[ii] > q[ii + 1]) or q[ii] > ii + 1:
            tmp = 0
            for jj in range(ii + 1, len(q)):
                if q[jj] < q[ii]:
                    tmp += 1
            if tmp > 2:
                print('Too Chaotic')
                br = 1
                break
            else:
                total += tmp
    if not br:
        print(total)

    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
