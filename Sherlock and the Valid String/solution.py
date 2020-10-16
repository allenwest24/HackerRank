#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    my_dict = {}
    norm = 0
    holder = []
    for ii in range(len(s)):
        if s[ii] not in my_dict:
            my_dict[s[ii]] = 0
        my_dict[s[ii]] += 1
    for jj in my_dict.values():
        holder.append(jj)
    holder.sort()
    norm = holder[0]
    for kk in range(len(holder)):
        if kk == len(holder) - 1:
            if (holder[kk] == norm + 1 or holder[kk] == norm):
                return "YES"
            else:
                return "NO"
        elif holder[kk] != norm:
                return "NO"
    return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
