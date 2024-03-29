import pytest

import n_ary_tree.levelorder_traversal as prob
import n_ary_tree.operations as n_tree

class TestLevelorderTraversal:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = [[1],[3,2,4],[5,6]]
    rootNode = n_tree.create(root)
    assert prob.levelOrder(rootNode) == res
  
  def test_example2(self):
    root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,
14]
    res = [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
    rootNode = n_tree.create(root)
    assert prob.levelOrder(rootNode) == res