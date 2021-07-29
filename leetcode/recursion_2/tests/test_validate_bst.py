import pytest

import binary_tree.operations as bTree
import recursion_2.validate_bst as prob


class TestValidateBst:
  def test_example1(self):
    root = [2,1,3]
    res = True
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res
  

  def test_example2(self):
    root = [5,1,4,None,None,3,6]
    res = False
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res
  

  def test_my_example1(self):
    root = [2,2,2]
    res = False
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res
  
  
  def test_my_example2(self):
    root = [5,1,6,None,None,4,7]
    res = False
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res
  

  def test_my_example3(self):
    root = [5,4,7,3,9,6,8]
    res = False
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res
  

  def test_my_example4(self):
    root = [4,2,6,1,3,5,7]
    res = True
    rootNode = bTree.create(root)
    assert prob.isValidBST(rootNode) == res