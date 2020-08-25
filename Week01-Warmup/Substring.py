# Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

# Examples:
# Input: laboratory, rat
# Output: true

# Input: cat, meow
# Output: false

#Understand
# 1. can I use build in function? -> No
# 2. Will second string always be shorter than the first? if not, how to handel? -> print invalid input

#Match
#blut force

#Plan
#let str1 be the longer string
#loop through str1
#compare str2 to left most of str1
#if same, return True
#if not, compare to next index of str1

#Implement
def Substring(str1, str2):
  len1, len2 = len(str1), len(str2)
  print(len1,len2)
  if len2 > len1:
    print('Invalid Input')
    return False
  else:
    for i in range(len1-len2+1):
      if str1[i:i+len2] == str2:
        return True
      else:
        continue
    return False

#Review
# Input: laboratory, rat
# Output: true
test1_str1 = 'laboratory'
test1_str2 = 'rat'
print(Substring(test1_str1, test1_str2), '| Expected: True')

# Input: cat, meow
# Output: false
test2_str1 = 'cat'
test2_str2 = 'meow'
print(Substring(test2_str1, test2_str2), '| Expected: False')

#Evaluate
#Runtime = O(n)
#Space complexity =O(1)
#********************************
#  time spend: 23m 23s
#********************************
