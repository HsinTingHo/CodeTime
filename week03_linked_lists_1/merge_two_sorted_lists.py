# Problem 3 - Merge Two Sorted Lists
# Merge two sorted linked lists.

#Understand
#1. are all the data in list integers? -> yes
#2. does the solution need to be inplace? -> yes
#3. what to return? -> head of the merged list
#4. can traverse list multiple times?

#edge case:
# Input: 1->2->4, 1->3->4  
# Output: 1->1->2->3->4->4

#list1 is shorter
# Input: 1, 1->3->4  
# Output: 1->1->2->3->4->4

#list1 is longer
# Input: 1->2->8, 3->4  
# Output: 1->1->2->3->4->4

#Match:
#two pointers

#Plan:
#compare the data in both head and the one with bigger value will be merge into the one with smaller value
#let set the pointer at the smaller head list p1, and set it as new_head
#let set the other pointer p2
#while p1 and p2 are not None
#   while the p1 data is smaller or equal to p2 data, save p1 as previous and move p1 pointer
#   connect p2 node to list1, save p2 as previous and move p2 to next node on list2
#if p1 is not None and p2 is None: (if p2 is not None, previous is already pointing at list 2)
#.  connect previous with the rest of list1
#return new_head

def merge_two_sorted_lists(head1, head2):
  if head1 is not None and head2 is not None:
    
    if head1.data <= head2.data:
      new_head = p1 = head1
      p2 = head2
    else:
      new_head = p1 = head2
      p2 = head1
    
    previous = None
    while (p1 is not None) and (p2 is not None):
      print(p1.data)
      if p2 is not None:
        print('p2', p2.data)
      #insert bigger node(p2) into list1
      while (p1 is not None) and (p1.data <= p2.data):
        previous = p1
        p1 = p1.next
      previous.next = p2
      previous = p2
      p2 = p2.next
      previous.next = p1
    if p1 is not None and p2 is None:
      previous.next = p1
    return new_head

#Review:
import linked_list as l
# Input: 1->2->4, 1->3->4  
# Output: 1->1->2->3->4->4
list1 = [1,2,4]
list2 = [1,3,4]
input1 = l.S_List()
input2 = l.S_List()

for elem in list1:
  node = l.S_Node(elem)
  input1.insert(node)
for elem in list2:
  node = l.S_Node(elem)
  input2.insert(node)
result = merge_two_sorted_lists(input1.head, input2.head)
current = result
while current is not None:
  print(current.data)
  current = current.next
#list1 is shorter
# Input: 1, 1->3->4  
# Output: 1->1->2->3->4->4

#list1 is longer
# Input: 1->2->8, 3->4  
# Output: 1->1->2->3->4->4

#Evaluate:
#Runtime: O(m+n)
#Space:O(1)
#***************************
# total time 51m23s
#***************************