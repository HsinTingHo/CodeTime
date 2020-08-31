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

