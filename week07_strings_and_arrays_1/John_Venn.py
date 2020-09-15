# John Venn
# Programming challenge description:
# Write a program that accepts two sets of alpha-numeric characters and performs an efficient matching between them. Finally, display the results.

# The intent of this challenge is to play with set theory. Avoid using pre-built framework functions that perform this work in a single line of code. Instead, illustrate how you would efficiently operate with two sets of data when trying to match values between them.

# There are many ways to approach this algorithm so be creative.

# Input:
# Two lines of input, each with a space-delimited series of values that represent the two sets. For example:

# 1 2 3 A B C
# X 11 G M 2 9 3 C N R

# Output:
# The set of values that exist in both input sets sorted alpha-numerically. For example:

# C 2 3

# If no common values exist, output NULL

# Test 1
# Test Input
# 1 2 3 A B C
# X 11 G M 2 9 3 C N R

# Expected Output
# 2 3 C

# Test 2
# Test Input
# 6 0 2 4 7 1 8 3 9 5
# A1 3 G DOG 18 3 9 E BIRD ONE 5 U J X2

# Expected Output
# 3 5 9

# Test 3
# Test Input
# 1 2 3 4 5 6 7 8 9 0
# A B C D E F G

# Expected Output
# NULL

import sys

def to_sort(a_set):   
    return sorted(a_set)

def match(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    len_1 = len(set1)
    len_2 = len(set2)
    sorted_set1 = to_sort(set1)
    sorted_set2 = to_sort(set2)
    result = []
    if len_1<=len_2:
        outter, inner = sorted_set1, sorted_set2
    else:
        outter, inner = sorted_set2, sorted_set1

    index = 0
    for item1 in outter:
        for item2 in inner[index:]:
            if item1 == item2:
                index = inner.index(item2)
                result.append(item1)
        
           
    if len(result) > 0:
        return result
    else:
        return None

#Evaluate
#Runtime: O(n+m)
#Space: O(n)