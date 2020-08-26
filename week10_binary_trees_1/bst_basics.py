from collections import deque

class Node:
  def __init__(self,data):
    self.data = data
    self.parent = None
    self.left = None
    self.right = None

class BST:
  def __init__(self, node = None):
    self.root = node
    if node is not None:
      self.add_new_node(node)

  def add_new_node(self, node):
    #traverse through tree
    y = None #runner
    x = self.root
    while x is not None:
      y = x
      if node.data < x.data:
        x = x.left
      else:
        x = x.right

    #assign parent
    node.parent = y

    #add node
    if y is None:
      print('I am a real tree now!')
      self.root = node
    elif node.data<y.data:
      y.left = node
    else:
      y.right = node


  def print_tree(self):
    pass

def print_preorder(root):
  if root is not None:
    print(root.data)
    print_preorder(root.right)
    print_preorder(root.left)

def print_preorder_iter(root):
  '''
  Psuedocode
  1. create an empty stack and push root to the stack
  2. do following when stack is not empty
    a.pop item from stack and print it
    b.push right child of the popped item to stack
    c.push left child of the popped item to stack
  '''
  if root is not None:
    stack = deque()
    current = root
    stack.append(current)
    while stack:
      current = stack.pop()
      print(current.data)

      if current.right is not None:
        stack.append(current.right)

      if current.left is not None:
        stack.append(current.left)

def print_postorder(root):
  if root is not None:
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.data)

def print_postorder_iter(root):#left/right/root
  '''
  Psuedocode
  1. push root to first stack
  2. loop while first stack is not empty
    a. pop a node from first stack and push it to second stack
    b. push left and right children of the popped node to first stack
  3. print contents of second stack
  '''
  if root is not None:
    stack1 = deque()
    stack2 = deque()
    stack1.append(root)
    while stack1:
      temp = stack1.pop()
      stack2.append(temp)
      if temp.left is not None:
        stack1.append(temp.left)
      if temp.right is not None:
        stack1.append(temp.right)
    while stack2:
      print(stack2.pop().data)

def print_inorder(root):
  if root is not None:
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)

def print_inorder_iter(root):
  if root is not None:
    current = root
    stack = deque()
    while True:
      if current is not None:
        stack.append(current)
        current = current.left

      elif(stack):
        current = stack.pop()
        print(current.data)

        current = current.right
      else:
        print('Finished')
        break



#Test BST
test1 = [1]
test2 = [2,3,9,7,1]

tree2 = BST()
for i in test2:
  print('Adding node %d'%i)
  node = Node(i)
  tree2.add_new_node(node)
print('*** Done set up test data ***')
print_preorder_iter(tree2.root)
