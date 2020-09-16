# Problem #3: Increment an arbitrary precision integer

# Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.

# For example:

# Input: [1,2,3]
# Output: [1,2,4]

# Explanation: 123 + 1 = 124

# Input: [5,8,9]
# Output: [5,9,0]

# Explanation: 589 + 1 = 590

#Understand:
#if input is none or empty, return original input?

#Match:
#Plan:
#1. form a string from given array
#2. cast string to integer
#3. add 1 to integer
#4. cast integer to string
#5. form an array

def increment_precision(arr):
  if arr is None or len(arr)==0:
    return arr
  str_num = ''
  for elem in arr:
    str_num += str(elem)
  num = int(str_num)
  num += 1
  result = []
  temp = str(num)
  for char in temp:
    result.append(int(char))
  return result

#Evaluate 
#runtime = O(n)
#space = O(n)

