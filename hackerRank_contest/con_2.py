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

#outter = 2*inner
#outter can hold 1 inner

#Plan:
#2 pointers
#sort the list and find the closest number that is twice as large

def findDolls(size):
    size.sort()
    print(size)
    p1, p2 = 0, 1
    length = len(size)
    final_boxes = []
    count = 0
    box_table = {}

    for box in size:
        if box in box_table.keys():
            box_table[box] += 1
        else:
            box_table[box] = 1
    unique_b = box_table.keys()
    for box in unique_b:
        num_small_box = box_table[box]
        for another_box in unique_b:
            if another_box >= box*2:
                for i in range(box_table[another_box]):
                    print(box, another_box, count)
                    count += 1
                    box_table[another_box] -= 1
                break
    return count
    # while p1 < length and p2 < length:
    #     if size[p1]*2 <= size[p2]:
    #         final_box.append(size[p2])
    #         p1 += 1
    #         p2 += 1
    #     p2 += 1