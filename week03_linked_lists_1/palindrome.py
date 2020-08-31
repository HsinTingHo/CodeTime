# Problem 1 - Palindrome
# Given a linked list, determine if it is a palindrome. Your method would take in a linked list and return True / False for whether the list is a palindrome or not.

#Understand
#1. is this a singlely linked or doublely linked list? -> singlely
#2. am i allowed to pass the linked list multiple time? -> yes
#3. what is the argument of the function, list or head of list? -> head
#4. can I assume all the value in the linked list has same data type? -> yes

# edge case
# input: '121'
# output: True

# input: 'arfd'
# output: False

# input: ''
# output: None

#Plan
#troverse list once to get the mid point of the list
#store the first half data of the linked list in an array
#compare the first half and the second half of the linked list
import linked_list as l
def palindrome(head):
  if head is None:
    return None
  current = head
  length = 0
  first_half = []
  odd = False
  while current is not None:
    length += 1
    current = current.next
  if length%2 != 0:
    odd = True
  mid = length//2
  print('mid: %d' %mid)

  current = head
  while current is not None:
    if mid > 0:
      first_half.append(current.data)
      mid -= 1
    else:
      if odd:
        odd = False
        current = current.next
      if current.data != first_half[-1]:
        return False
      else:
        first_half.pop()
    current = current.next
  return True

test = [1,2,1]
test_list = l.S_List()
for elem in test:
  node = l.S_Node(elem)
  test_list.insert(node)

print('Test1 list:')
test_list.print_list()

print('Function test:')
print(palindrome(test_list.head),' | Expected: True')

test = ['a','r','f','d']
test_list = l.S_List()
for elem in test:
  node = l.S_Node(elem)
  test_list.insert(node)

print('Test2 list:')
test_list.print_list()

print('Function test:')
print(palindrome(test_list.head),' | Expected: False')

test = []
test_list = l.S_List()
for elem in test:
  node = l.S_Node(elem)
  test_list.insert(node)

print('Test3 list:')
test_list.print_list()

print('Function test:')
print(palindrome(test_list.head),' | Expected: None')

#evaluate
#runtime: O(n)
#space: O(n)

#*********************************
# total time: 28m30s
#*********************************