import pytest

import binary_tree.preorder_traversal as prob
import binary_tree.operations as bTree

class TestPreorderTraversal:
  def test_example1(self):
    root = [1,None,2, None, None,3]
    res = [1,2,3]
    rootNode = bTree.createUsingFullList(root)
    assert prob.preorderTraversal(rootNode) == res