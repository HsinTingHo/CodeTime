# Problem 2 - Detect Cycle
# Given a linked list, determine if it has a cycle in it. For this problem, it may be helpful for you to write some pseudocode on how to build a linked list with a cycle. A linked list with a cycle may look something like:

#Understand:
#1. is the linked list singlely linked? -> yes
#2. are data store in each node unique? -> no
#3. is the head of list the argument of the function? -> yes

#edge case:
#has cycle
#does not have cycle
#empty list

#Match:
#1. brute force

#Plan:
#traverse through the link list and save the memory address of each node in a set. if the lengh of the set changes, the node has not been visited, otherwize, there exists a cycle

import linked_list as l

def detect_cycle(head):
  if head is None:
    return False

  id_set = set()
  current = head
  id_set.add(id(current))
  current = current.next
  set_size = len(id_set)
  while current is not None and current is not head:
    id_set.add(id(current))
    if set_size == len(id_set):#no change in set set_size
      return True
    current = current.next
    
  if current is None:
    return False
  else:
    return True

test = [1,2,3,4,5]
test_list1 = l.S_List()
for elem in test:
  node = l.S_Node(elem)
  test_list1.insert(node)
print(detect_cycle(test_list1.head), '| Expected: False')

test_list = l.S_List()
print(detect_cycle(test_list.head), '| Expected: False')

test_list = l.S_Cycle_List()
for elem in test:
  node = l.S_Node(elem)
  test_list.insert(node)
print(detect_cycle(test_list.head), '| Expected: True')

#evaluate
#runtime: O(n)
#space: O(n)

#****************************
#  total time: 35m47s
#****************************