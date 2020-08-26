# Problem 1 - Find a pair with given sum
# Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x.

#Understand
# 1. Return a boolean?
# test cases:
#.   input: [1,2,3,4], x=3
#.   output: True

#.   input:[3,4,5,2], x= 2
#.   output: False

#Match

#Plan
#if array is not empty
#sum up the first two element array and compare the sum with x
#if they are the same, return True. return False otherwise

def pair_with_given_sum(arr, x):
  length = len(arr)
  if length > 0:
    if arr[0]+arr[1] == x:
      return True
    else:
      return False

#review
test1=[1,2,3,4]
x = 3
print(pair_with_given_sum(test1, x), '| Expected: True')

test2=[3,4,5,2]
x = 2
print(pair_with_given_sum(test2, x), '| Expected: False')

#Evaluate
#Runtime: O(1)
#Space: O(1)

#************************************
# total time: 8m 17s
#************************************
