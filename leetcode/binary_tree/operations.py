from binary_tree.node import Node

import pdb

def createUsingFullList(in_list):
  """
  Create a Binary Tree from input list and return root.
  The binary tree in list form is as follows:
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

