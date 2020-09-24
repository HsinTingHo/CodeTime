# Problem 2: Insert into a Binary Search Tree
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.

#Plan:
#1. if root node is empty, set root node data to value
#2. comapare value with node data and traverse down to the tree until find suitable position(using while loop until reach a leaf)
#3. when insert:
#     a. node's parent
#     b. parent's left or right child

class Node:
  def __init__(self, value):
    self.data = value
    self.left = None
    self.right = None
    self.parent = None

def print_preorder(root):
  if root is not None:
    print(root.data)
    print_preorder(root.left)
    print_preorder(root.right)

def insert(root, value):
  node = Node(value)
  if root is None:
    root = node
    return root
  else:
    current = root
    while current is not None:
      parent = current
      if current.data > value:
        current = current.left
      elif current.data < value:
        current = current.right
    if parent.data > value:
      parent.left = node
    elif parent.data < value:
      parent.right = node
    node.parent = parent
    return root

#test
import bst_basics as bb
tree = bb.BST()
tree.root = insert(tree.root, 3)
print_preorder(tree.root)
print('another test')
insert(tree.root, 5)
print_preorder(tree.root)

#Evaluate
#Runtime: O(lgn)
#Space: O(1)


#**********************
# total time: 30m 42s
#**********************