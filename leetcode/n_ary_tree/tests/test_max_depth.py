import pytest

import n_ary_tree.max_depth as prob
import n_ary_tree.operations as n_tree

class TestMaxDepth:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = 3
    rootNode = n_tree.create(root)
    assert prob.maxDepth(rootNode) == res
  
  def test_example2(self):
    root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,
14]
    res = 5
    rootNode = n_tree.create(root)
    assert prob.maxDepth(rootNode) == res