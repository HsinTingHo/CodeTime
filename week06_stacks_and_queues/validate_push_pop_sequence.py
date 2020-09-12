# Problem 2 - Validate push/pop sequences of Stack
# Given push and pop sequences with distinct values, check if this could have been the result of a sequence of push and pop operations on an initially empty stack.

# Example:

# Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# Output: True

# Following sequence can be performed:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Input: pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# Output: False

# 1 can't be popped before 2.

#Understand
#1. will the input be two arrays?


#Plan
#initiate an array called stack
#to_check index = 0
#Loop through to_push
#   if same to the current to_check element
#     to_check_index += 1
#.  else, push element to stack
#loop through the rest of to_check
#   if element is on top of stack
#.      pop stack
#.  else, return False
#return True

def validate_push_and_pop_sequence(to_push, to_check):
  if to_push is not None and to_check is not None:
    if len(to_push) != len(to_check):
      return False
    stack = []
    check_i = 0
    for elem in to_push:
      if elem == to_check[check_i]:
        check_i += 1
      else:
        stack.append(elem)
  
    for i in range(check_i, len(to_check)):
      if to_check[i] != stack.pop():
        return False
    return True

#evaluate
#Runtime: O(n)
#Space: O(n)
#**************************
# total time: 25m58s
#test
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(validate_push_and_pop_sequence(pushed, popped))