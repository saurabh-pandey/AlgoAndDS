import pytest

import binary_tree.preorder_traversal as prob
import binary_tree.operations as bTree

class TestPreorderTraversal:
  def test_example1_1(self):
    root = [1,None,2, None, None,3]
    res = [1,2,3]
    rootNode = bTree.createUsingCompleteList(root)
    assert prob.preorderTraversal(rootNode) == res
  

  def test_example1_2(self):
    root = [1,None,2,3]
    res = [1,2,3]
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode) == res
  

  def test_example1_iterative(self):
    root = [1,None,2,3]
    res = [1,2,3]
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode, False) == res
  

  def test_example2(self):
    root = []
    res = []
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode) == res
  

  def test_example3(self):
    root = [1]
    res = [1]
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode) == res
  

  def test_example4(self):
    root = [1,2]
    res = [1,2]
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode) == res
  

  def test_example5(self):
    root = [1, None, 2]
    res = [1,2]
    rootNode = bTree.create(root)
    assert prob.preorderTraversal(rootNode) == res