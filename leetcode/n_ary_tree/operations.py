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
  
  root = Node(in_list[0])
  if len(in_list) > 1:
    assert in_list[1] is None
  val_queue = in_list[1:]
  nodes_queue = [root]
  parent_node = None
  while len(val_queue) > 0:
    curr_val = val_queue.pop(0)
    if curr_val is None:
      parent_node = nodes_queue.pop(0)
    else:
      assert parent_node is not None, "Parent node None"
      child_node = Node(curr_val)
      parent_node.children.append(child_node)
      nodes_queue.append(child_node)
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