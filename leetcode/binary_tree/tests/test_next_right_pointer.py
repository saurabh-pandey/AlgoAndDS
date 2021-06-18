import pytest

import binary_tree.next_right_pointer as prob

def create(in_list):
  if len(in_list) == 0:
    return None
  if in_list[0] == None:
    return None
  
  val_queue = in_list[1:]
  root = prob.Node(in_list[0])
  nodes_queue = [root]
  while len(val_queue) > 0:
    leftVal = None if len(val_queue) == 0 else val_queue.pop(0)
    rightVal = None if len(val_queue) == 0 else val_queue.pop(0)

    currNode = nodes_queue.pop(0)
    if leftVal is not None:
      leftNode = prob.Node(leftVal)
      currNode.left = leftNode
      nodes_queue.append(leftNode)
    if rightVal is not None:
      rightNode = prob.Node(rightVal)
      currNode.right = rightNode
      nodes_queue.append(rightNode)
  return root


def getNextRightList(root):
  if root is None:
    return []
  
  nextRightList = []
  nodes_queue = [root]
  while len(nodes_queue) > 0:
    node = nodes_queue.pop(0)
    nextRightList.append(node.val)
    if node.next is None:
      nextRightList.append(None)
    if node.left is not None:
      nodes_queue.append(node.left)
    if node.right is not None:
      nodes_queue.append(node.right)
  return nextRightList

class TestNextRightPointer:
  def test_example1(self):
    root = [1,2,3,4,5,6,7]
    rootNode = create(root)
    res = [1,None,2,3,None,4,5,6,7,None]
    newRootNode = prob.connect(rootNode)
    assert res == getNextRightList(newRootNode)
