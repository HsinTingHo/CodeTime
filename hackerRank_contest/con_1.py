#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
#Problem 1:
#There is an algorith that shift the character in a given string to left and store in a list, one at a time, until the string is the original string.
#Count how many string in the list has same starting character and ending character

def countStrings(s):
    #check if s is empty
    if s is None or s == "":
        return 0
    
    #if not, continue to count
    #1. check if head and tail are the same
    #2. check if there is any adjecent items are the same
    count = 0
    if s[0] == s[-1]:
        count += 1
    s_arr = []
    s_arr[:0] = s
    
    for i in range(len(s_arr)-1):
        if s_arr[i] == s_arr[i+1]:
            count += 1
    return count