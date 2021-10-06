import pytest

import n_ary_tree.operations as n_tree
import n_ary_tree.postorder_traversal as prob

class TestPostorderTraversal:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = [5,6,3,2,4,1]
    rootNode = n_tree.create(root)
    assert prob.postorder(rootNode) == res
