# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

#Understand
# 1. how to handle sigle digit input?
#edge cases:
# input 3
# output
# Plan
# an array to store all the sums
# seperate each digit -> cast num to string, cast char to int
#sum the square of each int and assign it to n
#repeat until n is 1
#if sum is in array, return false
#retun true

def happy_number(n):
  sum_arr=[]
  time = 0
  while n != 1:
    time += 1
    char_arr = [i for i in str(n)]
    sum = 0
    for c in char_arr:
      sum += int(c)**2
    if sum in sum_arr:
      return False
    sum_arr.append(sum)
    n = sum
    print('time: %d'%time)
  return True

test = 19
print(happy_number(test),'| Expected: True')
test = 3
print(happy_number(test),'| Expected: False')


#*************************
#.  total time: 24m 27s
#*************************
