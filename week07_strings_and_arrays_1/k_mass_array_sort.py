#understand:
#When k = 0, means array is perfectly sorted?
#how to handle k > arr.length?
#return or print the result ?


#edge cases:
# Input: arr = [1,2] ; k = 3
# Output: 

# Input: arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#match:
#2 pointer race car

#Plan:
#if k greater than 0:
#p1 point first element
#p2 traverse through k element from p1
#   if p2 smaller than p1, swap
def sort_k_messed_array(arr, k):
  if k > 0:
    length = len(arr)
    p1 = p2 = 0
    while p1 < length:
      p2 = p1+1
      while p2 <= p1+k and p2 < length:
        if arr[p2]<arr[p1]:
          arr[p1], arr[p2] = arr[p2],arr[p1]
        p2 += 1
      p1 +=1
  return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
result = sort_k_messed_array(arr, k)
print(result)

#Evaluate
#Runtime = O(k*n)
#Space = O(1)

#*******************************
#  total time: 40m
#*******************************