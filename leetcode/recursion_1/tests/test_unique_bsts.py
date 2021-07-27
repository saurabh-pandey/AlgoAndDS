import pytest

import recursion_1.unique_bsts as prob

def toList(root):
  if root is None:
    return []
  
  treeList = [root.val]
  nodes_queue = [root]
  while len(nodes_queue) > 0:
    node = nodes_queue.pop(0)
    lChild = node.left
    rChild = node.right
    if lChild is None and rChild is None:
      continue
    if lChild is not None:
      treeList.append(lChild.val)
      nodes_queue.append(lChild)
    else:
      treeList.append(None)
    if rChild is not None:
      treeList.append(rChild.val)
      nodes_queue.append(rChild)
    else:
      treeList.append(None)
  # Remove trailing None
  while treeList[-1] == None:
    treeList.pop()
  return treeList

class TestUniqueBsts:
  def test_example1(self):
    n = 3
    res = [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]
    bsts = prob.generateTrees(n)
    resBsts = []
    for bst in bsts:
      resBsts.append(toList(bst))
    res.sort()
    resBsts.sort()
    assert res == resBsts
  

  def test_example2(self):
    n = 1
    res = [[1]]
    bsts = prob.generateTrees(n)
    resBsts = []
    for bst in bsts:
      resBsts.append(toList(bst))
    res.sort()
    resBsts.sort()
    assert res == resBsts
  

  def test_my_example1(self):
    n = 2
    res = [[2,1], [1,None,2]]
    bsts = prob.generateTrees(n)
    resBsts = []
    for bst in bsts:
      resBsts.append(toList(bst))
    res.sort()
    resBsts.sort()
    assert res == resBsts