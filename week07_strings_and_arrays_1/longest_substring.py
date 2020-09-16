# Problem Statement
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi"

#Understand:
#Match:
#shifting window

#Plan:
#if string is none or empty, return string
#set window size to the lengh of the string
#while window size > k,
#  while window is not at the end
#.    use set to fileter out the duplicate and count the length
#.       if the lengh < K, return window size
#.  decrement window size

def longest_substring(input_str, k):
  if input_str is None or len(input_str) == 0:
    return 0
  length = len(input_str)

  if length < k:
    return length

  window_size = length
  while window_size >= k:
    i = 0
    
    while i+window_size <= length:
      temp = set(input_str[i:window_size+i])
      if len(temp) <= k:
        return window_size
      i += 1
    window_size -= 1
    
  return window_size

#Evaluate
#runtime = O(n^2)
#space = O(n)

#***********************
# total time = 26m20s
#***********************