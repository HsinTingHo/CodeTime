# Write a function that reverses a string.

# Example:
# Input: "hello"
# Output: "olleh"

#Understand
# 1. will there be spacial characters such as '' in the string?
# 2. do we need to store the new string in a variable and return? -> up to you
# 3. can I use slicing -> no

#   edge cases:
#     1. empty string
#     2. special characters in string

#Match
# 1. print the string backwards with range()


def reverse_string(input_str):
  new_str = ''
  for i in range(len(input_str)-1, -1, -1):
    new_str += input_str[i]
  return new_str

#Review
test = 'hello'
print('Actual: ',reverse_string(test), '| Expected: olleh')

test2 = "I got a ' in the sentence"
print('Actual: ',reverse_string(test2), "| Expected: ecnetnes eht ni ' a tog I")


#Evaluate
#Runtime = O(n)
#Space complexity = O(1)
