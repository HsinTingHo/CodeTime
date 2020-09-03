# Problem 1 - Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: 2 -> 4 -> 3,  5 -> 6 -> 4
# Output: 7 -> 0 -> 8
#
# Explanation: 342 + 465 = 807

#Understand:
# Can I alter one of the list? -> no
# are we passing in list or head of the list? -> head
# return head or list? -> list

# edge case:
# Input: 2 -> 4 -> 3,  5 -> 6 -> 4
# Output: 7 -> 0 -> 8

# Input: 2 -> 4,  5 -> 6 -> 4
# Output: 7 -> 0 -> 5

# Input: 1 -> 2, 0
# Output: 1 -> 2

#Match:

#Plan:
#create a new siglely linked list
#p1 point at list1
#p2 point at list2
#iterate both list together by move both pointer forward until one pointer is None
# add the data of two nodes that are pointed at and carry
# if the sum is greater than 10, set carry to 1
# else set carry to 0
# store result in a new node and insert to result list
#if p1 is not None, connect result to p1
#if p2 is not none, connect result to p2
import linked_list as l

def add_two_numbers(head1, head2):
  result = l.S_List()
  p1 = head1
  p2 = head2
  carry = 0

  while (p1 is not None) and (p2 is not None):
    sum = p1.data + p2.data + carry
    if sum >= 10:
      sum -= 10
      carry = 1
    else:
      carry = 0

    node = l.S_Node(sum)
    result.insert(node)
    p1 = p1.next
    p2 = p2.next
  
  current = result.head
  while current.next is not None:
    current = current.next
  if p1 is not None:
    if carry == 1:
      p1.data += 1
    current.next = p1
  elif p2 is not None:
    if carry == 1:
      p2.data += 1
    current.next = p2
  
  return result

# edge case:
# Input: 2 -> 4 -> 3,  5 -> 6 -> 4
# Output: 7 -> 0 -> 8

# Input: 2 -> 4,  5 -> 6 -> 4
# Output: 7 -> 0 -> 5

# Input: 1 -> 2, 0
# Output: 1 -> 2
#review
input1 = [1,2]
input2 = [0]
test1 = l.S_List()
test2 = l.S_List()

for elem in input1:
  node = l.S_Node(elem)
  test1.insert(node)

for elem in input2:
  node = l.S_Node(elem)
  test2.insert(node)

print('test1')
test1.print_list()
print('test2')
test2.print_list()
print('result')
result = add_two_numbers(test1.head, test2.head)
result.print_list()

#Evaluate
#Runtime: O(n)  n is the size of the smaller list
#Space: O(m) m is the size of the bigger list

#***********************
#  total time: 31m 54s
#***********************