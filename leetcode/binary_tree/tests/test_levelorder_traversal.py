import pytest

import binary_tree.levelorder_traversal as prob
import binary_tree.operations as bTree

class TestPostorderTraversal:
  def test_example1_1(self):
    root = [3,9,20,None,None,15,7]
    res = [[3],[9,20],[15,7]]
    rootNode = bTree.createUsingCompleteList(root)
    assert prob.levelOrder(rootNode) == res
  

  def test_example1_2(self):
    root = [3,9,20,None,None,15,7]
    res = [[3],[9,20],[15,7]]
    rootNode = bTree.create(root)
    assert prob.levelOrder(rootNode) == res