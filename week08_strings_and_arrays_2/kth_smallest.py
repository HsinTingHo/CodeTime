# Given an array and a number k where k is less than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

# Examples:

# Input: [7, 10, 4, 3, 20, 15]
#        k = 3
# Output: 7

# Input: [7, 10, 4, 3, 20, 15]
#        k = 4
# Output: 10


#Understand:
#will there be a case where k is 0? No 
#can I use predifined function? No

#Match:

import heapq
def kth_smallest(arr, k):
  heap = []
  result = 0
  for elem in arr:
    heapq.heappush(heap, elem)
  for i in range(k):
    result = heapq.heappop(heap)
  return result

test = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(test, k), '| Expected: 7')

#Evaluate
#runtime: O(nlogn)
#space: O(n)
