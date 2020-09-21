#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findDolls' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY size as parameter.
#

#Problem:
#A new policy is in place for a warehouse to reduce the number of the box laying arround. The policy is as follow:
#A small box can only be put into a box at least twice of its size
#A box can only fit one box
#Given a list of box size, count how many box will there be after implement the new policy


#Edge case:
#Input: [2,4,1,6,7,3,3,8]
#Output: 4

#Input: [1, 1]
#Output: 2

#Input: []
#Output: 0

#Input: [2,2,3,3]
#Output: 4

#Input: [2,4,4,6,8,8]
#Output: 3
#outter = 2*inner
#outter can hold 1 inner

#Plan:
#sort size
#creat a dictionary that use size as key and number of boxes as value
#start from the highest number of box, and check if the next most common box is double of size or twice as small
#if it is, reduce the value of both boxes


def findDolls(size):
    size.sort()
    print(size)
    p1 = 0
    length = len(size)
    for p1 in range(size):
      p2 = p1+1
      for 

    
    # while p1 < length and p2 < length:
    #     if size[p1]*2 <= size[p2]:
    #         final_box.append(size[p2])
    #         p1 += 1
    #         p2 += 1
    #     p2 += 1