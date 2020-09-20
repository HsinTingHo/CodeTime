#!/bin/python3

import math
import os
import random
import re
import sys

#Problem:
#A manerger manage few teams of developers. The manerger is given a hiring budget to hire more developers to balance the team.
#the number of developers in each team is given in a list. For example,
#[5,4,1,4,3] and max hire is 2
#the manerger can hire 1 and put the new hire in team 5, so there are 3 team has 4 developers
#or, the maneger can hire 2 and put them in team 2 and 4, so there are 3 team has 5 devekopers.

#
# Complete the 'maxBalancedTeams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY developers
#  2. INTEGER maxNewHires
#
#Plan
#sort developers array
#store number of developer in a dic
#get the key that has the highest value
#check if we can make a one lesser team match within maxNewHire budget
def max_key(dic):
    max_v = 0
    result = 0
    for k in dic.keys():
        if dic[k] > max_v:
            max_v = dic[k]
            result = k
    return k
    
def maxBalancedTeams(developers, maxNewHires):
    developers.sort()
    dev_table = {}
    for d in developers:
        if d in dev_table.keys():
            d += 1
        else:
            dev_table[d] = 1
    print(dev_table)
    
    max_k = max_key(dev_table)
    to_be_add = max_k-1
    if dev_table[max_k] - dev_table[to_be_add] <= maxNewHires:
        maxNewHires - dev_table[max_k] - dev_table[to_be_add]
        dev_table[max_k] += 1
    return dev_table[max_k]