# Problem 1 - Reverse a doubly linkedlist in the group of given size
# Given a doubly linked list containing n nodes. The problem is to reverse every group of k nodes in the list.

# Example:

# Input: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8
#        k = 3
#Output: 3 <-> 2 <-> 1 <-> 6 <-> 5 <-> 4 <-> 8 <-> 7

#Understand:
#1. how to handel k > n? -> reverse the whole list
#2. how to handle k = 0? -> return original list
#3. Do we pass in a list or the head of a list? -> list
#4. what is the required return value? -> list
#5. how to handle n = 0? -> return original list

# edge cases
# Input: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8
#        k = 3
# Output: 3 <-> 2 <-> 1 <-> 6 <-> 5 <-> 4 <-> 8 <-> 7

# Input:1 <-> 2, k = 3
# Output: 2 <-> 1

# Input:1 <-> 2, k = 0
# Output:1 <-> 2

# Input: None, k = 1
# Output: None

#Match
#2 pointers

#Plan:
#if k = 0 or head is none, return original list
#set p1 to the head and p2 to head.next
#while p1 and p2 are not none
#.   set counter = 1
#    traverse list with p2 and increment counter until counter equal to k
#.   set temp to p2.next
#     reverse from p1 to p2, return new_h, new_t
#.    if p1 is head, set head to new_h, set old_t equals to new_t
#.    else, connect old_t to new_h
#     if temp is not None, set p1 equals temp and p2 equals to temp.next
#return list


def reverse(p1, p2):
  p1.pre = p2.next = None
  new_t = p1
  new_h = p2
  current = p1
  while current is not None:
    temp = current.pre
    current.pre = current.next
    current.next = temp
    current = current.pre
    
    
  return new_h, new_t
    
def reverse_list_in_given_size(d_list, k):
  #handel k = 0 and empty list
  if k == 0 or d_list.head is None:
    return d_list

  p1 = p2 = d_list.head
  new_h = new_t = old_h = old_t = None
  while p1 is not None and p2 is not None:
    
    #get nodes to reverse
    counter = 1

    while counter < k and p2.next is not None:
      p2 = p2.next
      counter += 1
    
    temp = p2.next
    new_h, new_t = reverse(p1, p2)

    #First kth nodes need to reset the head
    if p1 is d_list.head:
      d_list.head = new_h
      old_t = new_t
    else:
      old_t.next = new_h
      new_h.pre = old_t
      old_t = new_t
    if temp is not None:
      p1 = p2 = temp
    else:
      break
  return d_list


#Evaluate
#Runtime: O(n)
#Space: O(1)
#******************************************
# total time: 90m 14s + 18m 40s 
#             = 108m 54s
#******************************************

