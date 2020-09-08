from week05_review import reverse_list_in_given_size as r
from week05_review import doubly_linked_list as d
print('****** test reverse doubly linked list ******')
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

test = [1,2,3,4,5,6,7,8]
k = 3
test_list = d.D_List()
for elem in test:
  node = d.D_Node(elem)
  test_list.insert(node)

print('Print list from head to tail')
test_list.print_list()

print('Print list after reverse every k nodes')
result = r.reverse_list_in_given_size(test_list, k)
result.print_list()

#test doubly linked list
print('\n****** test doubly linked list ******')
test = [1,2,3,4]
test_list = d.D_List()
for elem in test:
  node = d.D_Node(elem)
  test_list.insert(node)
print('Print list from head to tail')
test_list.print_list()
print('Print list from tail to head')
current = test_list.tail
while current is not None:
  print(current.data)
  current = current.pre