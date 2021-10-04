import pytest

import n_ary_tree.operations as n_tree
import n_ary_tree.preorder_traversal as prob

class TestPreorderTraversal:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = [1,3,5,6,2,4]
    rootNode = n_tree.create(root)
    assert prob.preorderTraversal(rootNode) == res
