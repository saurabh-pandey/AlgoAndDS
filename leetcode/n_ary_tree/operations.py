from n_ary_tree.node import Node


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


def toList(root):
  """
  Create a BFS list from N-ary tree
  Here the list is of the form [Node, Node.child1, Node.child2] and all null branches are ignored. 
  Thus the array is not a complete tree representation
  """
  if root is None:
    return []
  
  treeList = []
  nodes_queue = [root]
  while len(nodes_queue) > 0:
    node = nodes_queue.pop(0)
    if node is not None:
      treeList.append(node.val)
      for child in node.children:
        nodes_queue.append(child)
  return treeList