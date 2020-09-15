# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted

# Example 4:

# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

#Understand
#1. will the array be consecutive? -> no

#Match
#2 pointers


#Plan
#handel empty array
#set index1 at the begining of the array
#move one at the time until hit the element that is not sorted, set index 1 backwards
#if index1 = length-1, reuturn 0
#set index2 at the end of the array
#move backwards one at the time until the element that is not decending, set index2 1 forward
#result = index2-index1+1
#sort index1 to index2
#if not sorted, repeat
#return result

def sort_by_smallest_subarry(arr):
  
  length = len(arr)
  if length == 0:
    return 0

  sorted_arr = sorted(arr)
  index1 = 0
  index2 = length-1

  while index1 < index2:
    if arr[index1] == sorted_arr[index1]:
      index1 += 1
    else:
      break

  if index1 == index2:
    return 0
  
  while index2 > 0:
    if arr[index2] == sorted_arr[index2]:
      index2 -= 1
    else:
      break
  return index2 - index1 + 1

#Evaluate:
#Runtime = O(n)
#Space = O(n)