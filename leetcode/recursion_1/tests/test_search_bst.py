import pytest

import recursion_1.search_bst as prob

def createBST(bstList):
  if len(bstList) == 0:
    return None
  
  root = prob.TreeNode(bstList[0])
  bstNodes = [root]
  for i in range(1, len(bstList)):
    childNode = prob.TreeNode(bstList[i])
    bstNodes.append(childNode)
    if i%2 == 1:
      parentNode = bstNodes[int((i - 1)/2)]
      parentNode.left = childNode
    else: # i%2 == 0
      parentNode = bstNodes[int((i - 2)/2)]
      parentNode.right = childNode
  return root


def toList(root):
  if root is None:
    return []
  
  nodes = [root]
  bstList = []
  while len(nodes) > 0:
    node = nodes.pop(0)
    bstList.append(node.val)
    if node.left is not None:
      nodes.append(node.left)
    if node.right is not None:
      nodes.append(node.right)
  return bstList

class TestSearchBST:
  def test_example1(self):
    root = [4,2,7,1,3]
    val = 2
    res = [2,1,3]
    rootNode = createBST(root)
    resNode = prob.searchBST(rootNode, val)
    assert toList(resNode) == res
  

  def test_example2(self):
    root = [4,2,7,1,3]
    val = 5
    res = []
    rootNode = createBST(root)
    resNode = prob.searchBST(rootNode, val)
    assert toList(resNode) == res