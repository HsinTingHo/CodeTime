class S_Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class S_List:
  def __init__(self):
    self.head = None
  
  def insert(self, node):
    if self.head is None:
      self.head = node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = node

  def print_list(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next


#********************************
#  total time: 3m22s
#********************************


#A single linked list with tail connected to head to form a cycle
class S_Cycle_List:
  def __init__(self):
    self.head = None
    
  def insert(self, node):
    if self.head is None:
      self.head = node
      self.head.next = self.head
    else:
      current = self.head
      while current.next is not self.head:
        current = current.next
      current.next = node
      node.next = self.head

  def print_list(self):
    current = self.head
    while current.next is not self.head:
      print(current.data)
      current = current.next
    print(current.data)
    print('tail connected to ',current.next.data)
    
# print('***** Test Cycle List *****')
# test = [1,2,3,4,5]
# cycle_list = S_Cycle_List()
# for elem in test:
#   node = S_Node(elem)
#   cycle_list.insert(node)
# cycle_list.print_list()
#********************************
#  total time: 6m
#********************************