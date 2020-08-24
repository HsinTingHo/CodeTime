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

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
class Single_List:
  def __init__(self):
    self.head = None


#test cases:
new_list1 = Single_List()
new_list2 = Single_List()
new_lists = [new_list1, new_list2]

test_input1 = [9,9]
test_input2 = [9,9]
inputs=[test_input1, test_input2]


for index, each_input in enumerate(inputs):
  count = 0
  for num in each_input:
    node = Node(num)
    if count == 0:
      new_lists[index].head = node
      current = new_lists[index].head
    else:
      current.next = node
      current = current.next
    count += 1

#print out list content to varify the list constructed correctly
# for each_list in new_lists:
#   current = each_list.head
#   while current is not None:
#     print(current.data)
#     current = current.next
# Problem 1 - Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: 2 -> 4 -> 3,  5 -> 6 -> 4
# Output: 7 -> 0 -> 8

# Explanation: 342 + 465 = 807


#Understand
# does both linked list has same length?
# inplace? - No

# Input 0->0->0, 0->0->0
# Output 0->0->0

# Input 9->9, 9->9
# Output 8->9->1

#Match
#   run through multiple times
# v Dummy nodes

#Plan
#loop through the lists and add each node up
#if dummy.data is one
#sum = test_data1+test_data2+1
#set dummy node to 0
#else
#sum = test_data1+test_data2
#if the sum is greater than 9, set dummy.data to 1
#create a new node with sum and add to linked list
#After loop, if the dummy node is 1, add dummy node to the end of list
#return list

#Implement
def Add_Two_Numbers(input1, input2):
  current1 = input1.head
  current2 = input2.head
  new_list = Single_List()
  current = new_list.head
  dummy = Node(0)
  count = 0
  while (current1 is not None) and (current2 is not None):
    num = current1.data + current2.data
    if dummy.data == 1:
      num += 1
      dummy.data = 0

    if num > 9:
      dummy.data = 1
      new_node = Node(num-10)
    else:
      new_node = Node(num)

    if count == 0:
      new_list.head = new_node
      current = new_list.head
    else:
      current.next = new_node
      current = current.next
    current1 = current1.next
    current2 = current2.next
    count += 1

  if dummy.data == 1:
    current.next = dummy
  return new_list


result = Add_Two_Numbers(new_list1,new_list2)
current = result.head
while current is not None:
  print(current.data)
  current = current.next

#Review

#Evaluate
#runtime of the solution: O(n)
#space complexity: O(n)
