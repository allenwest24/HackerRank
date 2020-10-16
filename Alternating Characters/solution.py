#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    total = 0
    curr = ''
    for letter in range(len(s)):
        if letter == 0:
            curr = s[letter]
        elif s[letter] == curr:
            total += 1
        else:
            curr = s[letter]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
