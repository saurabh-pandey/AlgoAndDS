from binary_tree.node import Node

import pdb

def createUsingCompleteList(in_list):
  """
  Create a Binary Tree from input list and return root.
  The binary tree in list form is assumed to be a complete tree , with if needed also filled with 
  None values, as follows:
  tree_as_list = [r, r.l, r.r, r.l.l, r.l.r, r.r.l, r.r.r, ...]
  """
  # pdb.set_trace()
  if len(in_list) == 0:
    return None
  
  nodes = []
  for val in in_list:
    if val is not None:
      nodes.append(Node(val))
    else:
      nodes.append(None)
  
  numNodes = len(nodes)
  for i in range(numNodes):
    node = nodes[i]
    if node is not None:
      leftNodeIndex = 2*i + 1
      rightNodeIndex = 2*i + 2
      if leftNodeIndex < numNodes:
        node.left = nodes[leftNodeIndex]
      if rightNodeIndex < numNodes:
        node.right = nodes[rightNodeIndex]
  return nodes[0]

def create(in_list):
  """
  Create a Binary Tree from input list and return root.
  Here the list is of the form [Node, Node.Left, Node.Right] and all null branches are ignored. Thus
  the array is not a complete tree representation
  """
  if len(in_list) == 0:
    return None
  if in_list[0] == None:
    return None
  
  val_queue = in_list[1:]
  root = Node(in_list[0])
  nodes_queue = [root]
  while len(val_queue) > 0:
    leftVal = None if len(val_queue) == 0 else val_queue.pop(0)
    rightVal = None if len(val_queue) == 0 else val_queue.pop(0)

    currNode = nodes_queue.pop(0)
    if leftVal is not None:
      leftNode = Node(leftVal)
      currNode.left = leftNode
      nodes_queue.append(leftNode)
    if rightVal is not None:
      rightNode = Node(rightVal)
      currNode.right = rightNode
      nodes_queue.append(rightNode)
  return root