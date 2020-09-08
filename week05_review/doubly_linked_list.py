class D_Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.pre = None

class D_List:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      node.pre = self.tail
      self.tail = node
  
  def print_list(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next
