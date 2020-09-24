# Problem 3: List to a balanced BST
# Create a balanced BST from an array. Output tree should be a valid BST and balanced. Balanced tree can have the difference of at most ONE between left and right.

#Plan:
#sort the array
#recursively, find the mid point of array and make it root

import bst_basics as bb
def list_to_balanced_tree(list):
  list.sort()
  length = len(list)
  if length > 0:
    mid = length//2
    node = bb.Node(list[mid])
    node.left = list_to_balanced_tree(list[0:mid])
    node.right = list_to_balanced_tree(list[mid+1:])
    return node


#test
test = [1,2,3,4]
node = list_to_balanced_tree(test)
bb.print_preorder(node)

#Evaluate
#Runtime = O(nlgn)
#Space = O(nlogn)