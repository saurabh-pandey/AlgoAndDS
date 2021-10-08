import pytest

import n_ary_tree.operations as n_tree
import n_ary_tree.preorder_traversal as prob

class TestPreorderTraversal:
  def test_example1(self):
    root = [1,None,3,2,4,None,5,6]
    res = [1,3,5,6,2,4]
    rootNode = n_tree.create(root)
    assert prob.preorder(rootNode) == res
  
  def test_example2(self):
    root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,
14]
    res = [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
    rootNode = n_tree.create(root)
    assert prob.preorder(rootNode) == res
  

