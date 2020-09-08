from week05_review import doubly_linked_list as d

#test doubly linked list
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