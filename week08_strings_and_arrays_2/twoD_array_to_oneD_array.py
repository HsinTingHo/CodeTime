# Convert a n x m 2D array into a (n * m) x 1 1D array.
#Understand:
#how to handel empty or null? -> return input array

#Plan:
#loop through rows and use extend

def twoD_array_to_oneD_array(arr):
  if arr is None or len(arr) == 0 or type(arr[0]) != type([]):
    return arr
  
  result = []
  
  for row in arr:
    result.extend(row)
  return result

#test

test = [[1,1,1],[2,2,2],[3,3,3]]
print(type(test))
print(twoD_array_to_oneD_array(test))
test = [1,1,1,2,2]
print(twoD_array_to_oneD_array(test))
test = []
print(twoD_array_to_oneD_array(test))
test = None
print(twoD_array_to_oneD_array(test))

#Evaluate
#runtime: O(n)
#Space: O(n*m)

#************************
# Total time: 13m 11s
#************************