# Problem #2: Run Length Encoding

# Given an input string, write a function that returns the run-length encoded string for the input string.

# For example:

# Input: "wwwwaaadexxxxxx"
# Output: "w4a3d1e1x6"

# Input: ""
# Output: ""
#Understand:
#1.will integer always < 10? -> yes

#Match:
#1.brute force

#Plan:
#0. if input is empty or null, return input
#1. initiate a dictionary
#2. loop through each char in input string
#2-1.   if char, if not in dictionary, save it and assign value of 1
#2-2.            if in dictionary, incriment value by 1
#3. loop through dictionary to create output

def run_length_encoding(input_str):
  if input_str is None or len(input_str) == 0:
    return input_str
  char_table = {}
  
  for char in input_str:
    if char in char_table:
      char_table[char] += 1
    else:
      char_table[char] = 1
  
  result = ''
  for key in char_table.keys():
    num = char_table[key]
    result += key + str(num)

  return result

#Evaluate
#runtime: O(n)
#space: O(n)

#**************************
# total time: 21m 30s
#**************************
