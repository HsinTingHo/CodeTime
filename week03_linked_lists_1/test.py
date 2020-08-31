import linked_list as l

test = [1,2,3,4,5, 'done!']
new_s_list = l.S_List()
for elem in test:
  node = l.S_Node(elem)
  new_s_list.insert(node)
new_s_list.print_list()