#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    avg = 0
    tmp = 0
    alerts = 0
    if d > len(expenditure) + 1:
        return 0
    for ii in range(d, len(expenditure)):
        for jj in range(ii - d, ii):
            tmp += expenditure[jj]
        avg = tmp / d
        tmp = 0
        if expenditure[ii] >= avg * 2:
            alerts += 1
        avg = 0
    return alerts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
