import pytest

import binary_tree.postorder_traversal as prob
import binary_tree.operations as bTree

class TestPostorderTraversal:
  def test_example1_1(self):
    root = [1,None,2, None, None,3]
    res = [3,2,1]
    rootNode = bTree.createUsingCompleteList(root)
    assert prob.postorderTraversal(rootNode) == res
  

  def test_example1_2(self):
    root = [1,None,2,3]
    res = [3,2,1]
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode) == res
  

  def test_example1_iterative(self):
    root = [1,None,2,3]
    res = [3,2,1]
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode, False) == res
  

  def test_example2(self):
    root = []
    res = []
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode) == res
  

  def test_example3(self):
    root = [1]
    res = [1]
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode) == res
  

  def test_example4(self):
    root = [1,2]
    res = [2,1]
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode) == res
  

  def test_example5(self):
    root = [1, None, 2]
    res = [2,1]
    rootNode = bTree.create(root)
    assert prob.postorderTraversal(rootNode) == res