# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

 

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

#Understand:
# input:1->2->3->4
# output: 2->1->4->3

# input:1->2->3
# output: 2->1->3

# input: 1
# output: 1

#match
#two pointer

#Plan
#p1 points at head, p2 points to head.next
#in each iteration, swap these 2 nodes and move both pointers 2 nodes foward
def swap(pre, p1, p2):
  if pre is not None:
    pre.next = p2
  temp = p2.next
  p2.next = p1
  p1.next = temp
  pre = p1
  return pre

def swap_nodes_in_pairs(head):
  if head is not None:
    p1 = head
    p2 = head.next
    pre = None
    while (p1 is not None) and (p2 is not None):
      if p1 is head:
        head = p2
      pre = swap(pre, p1, p2)
      p1 = p1.next
      if p1 is not None:
        p2 = p1.next
  return head

#review
import linked_list as l
test1 = [1,2,3,4]
test_list = l.S_List()
for elem in test1:
  node = l.S_Node(elem)
  test_list.insert(node)
print('*** Before swap ***')
test_list.print_list()
print('*** After swap ***')
test_list.head = swap_nodes_in_pairs(test_list.head)
test_list.print_list()

#evaluate
#runtime: O(n)
#space: O(1)

#*************************
#. total time: 38m
#*************************

