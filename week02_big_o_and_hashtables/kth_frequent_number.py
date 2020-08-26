# Problem 2 - Kth frequent number
# Find the element that appears k number of times in an array.

# Input: [8, 7, 9, 6, 7, 5, 1], k = 2
# Output: 7

#Understand
#1. can I use build in function such as count? -> No
#2. how to handle k > lenth of the array? -> print invalid input
#3. how to handel no element appears k number of times?
#.  -> print no element appear k times
#4. how to handel more than one element appears
#   k number of times? -> print them all out

#test cases:
# Input: [8, 7, 9], k=4
# Output: invalid input

# Input: [8, 7, 9, 6, 7, 5, 1], k = 2
# Output: 7

# Input: [8, 7, 9, 6, 7, 5, 1], k = 4
# Output: no element appear k times

# Input: [8, 7, 9, 6, 7, 5, 1], k = 1
# Output: [8,9,6,5,1]

#Match:
#1. hachmap

def kth_frequent_number(arr, k):
  length=len(arr)
  if length < k:
    print('Invalid Input')
    return

  #create a dictionary
  dic = {}
  k_elem = []
  for elem in arr:
    if dic.get(elem):
      dic[elem] += 1
    else:
      dic[elem] = 1
  for key in dic.keys():
    if dic[key] == k:
      k_elem.append(key)
  if len(k_elem) == 0:
    print('no element appear k times')
  return(k_elem)

#Review
test = [8, 7, 9]
k=4
print(kth_frequent_number(test, k), '| Expected: invalid input')


test = [8, 7, 9, 6, 7, 5, 1]
k = 2
print(kth_frequent_number(test, k), '| Expected: 7')


test= [8, 7, 9, 6, 7, 5, 1]
k = 4
print(kth_frequent_number(test, k), '| Expected: no element appear k times')

test = [8, 7, 9, 6, 7, 5, 1]
k = 1
print(kth_frequent_number(test, k), '| Expected: [8,9,6,5,1]')

#Evaluate
#Runtime = O(n)
#Space = O(n)

#*********************************
# total time: 21m
#*********************************
