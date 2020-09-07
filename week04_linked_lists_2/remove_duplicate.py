# Problem 4 (Challenge!) - Remove Duplicates
# Given a linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Can you do it without taking up extra memory?

# Examples:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Input: 1->1->1->2->3
# Output: 2->3

#Understand
#1. will all the numbers in the list be integers? -> y
#2. will the list be sorted? -> y
#3. head of list as parameter? return the head? -> y
#4. edge cases
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Input: 1->1->1->2->3
# Output: 2->3

#Match:
#two pointers

#Plan:
#p1 point at head and p2 points at p1's next node
#set pre to None
#while p2 is not None
#.   if p1 data = p2 data
#.    keep moving p2 until p2 data is not equal to p1 data
#.    if p1 is head, set p2 to head
#.    else, connect pre to p2
#.   else, set pre to p1 and move p1 and p2 to next

def remove_duplicate(l_list):
  if l_list.head is not None:
    p1 = l_list.head
    p2 = p1.next
    pre = None
    while p2 is not None:
      if p1.data == p2.data:
        while p2.data == p1.data:
          p2 = p2.next
          if p2 is None:
            if pre is not None:
              pre.next = None
            else:
              l_list.head = None
            break
            
        if p1 is l_list.head:
          l_list.head = p2
        else:
          if p2 is None and pre is None:
            return None
            
          pre.next = p2
          p1 = p2
          p2 = p2.next
      else:
        pre = p1
        p1 = p1.next
        p2 = p2.next
    return l_list

#Review
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Input: 1->1->1->2->3
# Output: 2->3

# Input: 1->1->1->2->3->3
# Output: 2

# Input: 1->1->1
# Output: None

import linked_list as l
test_list = l.S_List()
test_data = [1,1,1]
for elem in test_data:
  node = l.S_Node(elem)
  test_list.insert(node)
print('Before remove')
test_list.print_list()
print('After remove')
result = remove_duplicate(test_list)
if result is not None:
  result.print_list()
else:
  print('whole list are duplicated elements')

#Evaluate
#Runtime: O(n)
#Space: O(1)

#*********************
# total time: 43m50s
#*********************