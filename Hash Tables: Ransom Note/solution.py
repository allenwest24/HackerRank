#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    freq_holder = {}
    for word in magazine:
        if word not in freq_holder:
            freq_holder[word] = 0
        freq_holder[word] += 1
    for string in note:
        if string not in freq_holder:
            print("No")
            return
        else:
            if freq_holder[string] == 1:
                freq_holder.pop(string)
            else:
                freq_holder[string] -= 1
    print("Yes")
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
