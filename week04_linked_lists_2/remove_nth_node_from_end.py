# Problem 2 - Remove Nth Node from End of List
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Input: 1->2->3->4->5, n = 2
# Output: 1->2->3->5

# Explanation: We remove the second node from the end, the node with value 4

#Understand
#1. parameter is a list or the head of list?
#2. edge cases
# Input: 1->2->3->4->5, n = 2
# Output: 1->2->3->5

# n is greater than the length of the list 
# Input: 1->2->3->4->5, n = 6
# Output: "Invalid Input"
#Match
#multi run through

#Plan
#travese the list and get the lengh of the list
#traverse the list again until reach the (lengh - n)-1 th node
#save node as pre
#go to next node, and save its next to temp
#connect pre and temp
#return the head of the list
def get_length(head):
  if head is None:
    return 0
  current = head
  length = 0
  while current is not None:
    current = current.next
    length += 1
  return length


def remove_nth_node_from_end(head, n):
  length = get_length(head)
  if n > length:
    print('Invalid Input')
    return
  count = 0
  pre = None
  current = head
  while count < (length - n):
    pre = current
    current = current.next
    count += 1
  current = current.next
  pre.next = current
  return head

#Review
import linked_list as l
test = l.S_List() 
input1 = [1,2,3,4,5]
n = 2
for elem in input1:
  node = l.S_Node(elem)
  test.insert(node)
print('Before remove')
test.print_list()
print('After remove')
result = remove_nth_node_from_end(test.head, n)
test.print_list()

#Evaluate
#Runtime = O(n)
#Space = O(1)

#**********************
# total time: 29m 30s
#**********************