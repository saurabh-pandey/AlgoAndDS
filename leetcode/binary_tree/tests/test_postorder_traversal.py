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