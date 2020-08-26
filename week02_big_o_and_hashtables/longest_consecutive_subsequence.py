# Problem 3 (Challenge) - Longest Consecutive Subsequence
# Given an unsorted array of integers, we want to find the length of the longest subsequence such that elements in the subsequence are consecutive integers. The consecutive numbers can be in any order.



#Understand
#1. if there is no consecutive subsequence, do we return 1? -> yes
#2. is there space constrain? -> no
#3. can I modify the original array? -> yes
#test cases
# Input: [1, 9, 3, 10, 4, 20 , 2]
# Output: 4

# Input: [1, 9, 12, 10, 3, 20 , 5]
# Output: 1

#Match
#sort and find the consequetive sebsequence

#Plan
#sort the array
#set longest to 1
#looped through the sorted array, if the nuber is consecutive, incriment longest
#else, set longest to 1
def longest_consecutive_subsequence(arr):
  arr.sort()
  record =[]
  longest = 1
  for i in range(len(arr)-2):
    if arr[i] == (arr[i+1]-1):
      longest += 1
    else:
      longest = 1
    record.append(longest)
  return max(record)

#review
input= [1, 9, 3, 10, 4, 20 , 2]
print(longest_consecutive_subsequence(input), '| Expected: 4')

input= [1, 9, 12, 3, 20 , 5]
print(longest_consecutive_subsequence(input), '| Expected: 1')

#Evaluate
#Runtime: O(n)
#complexity: O(n)

#**********************************
#   total time: 19m 10s
#**********************************
