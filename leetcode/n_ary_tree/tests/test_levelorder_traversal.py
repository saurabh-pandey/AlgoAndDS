import pytest

import n_ary_tree.levelorder_traversal as prob
import n_ary_tree.operations as n_tree

class TestLevelorderTraversal:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = [[1],[3,2,4],[5,6]]
    rootNode = n_tree.create(root)
    assert prob.levelOrder(rootNode) == res