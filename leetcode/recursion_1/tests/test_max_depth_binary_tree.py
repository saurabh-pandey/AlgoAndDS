import pytest

import binary_tree.operations as bTree
import recursion_1.max_depth_binary_tree as prob


class TestMaxDepthBinaryTree:
  def test_example1(self):
    root = [3,9,20,None,None,15,7]
    res = 3
    rootNode = bTree.create(root)
    assert prob.maxDepth(rootNode) == res
  

  def test_example2(self):
    root = [1,None,2]
    res = 2
    rootNode = bTree.create(root)
    assert prob.maxDepth(rootNode) == res
  

  def test_example3(self):
    root = []
    res = 0
    rootNode = bTree.create(root)
    assert prob.maxDepth(rootNode) == res
  

  def test_example4(self):
    root = [0]
    res = 1
    rootNode = bTree.create(root)
    assert prob.maxDepth(rootNode) == res