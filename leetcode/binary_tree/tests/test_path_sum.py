import pytest

import binary_tree.path_sum as prob
import binary_tree.operations as bTree

class TestPathSum:
  def test_example_1(self):
    root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22
    res = True
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res
  

  def test_example_2(self):
    root = [1,2,3]
    targetSum = 5
    res = False
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res
  

  def test_example_3(self):
    root = [1,2]
    targetSum = 0
    res = False
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res
  

  def test_lc_run_1(self):
    root = [1,2]
    targetSum = 1
    res = False
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res
  

  def test_lc_run_2(self):
    root = [1]
    targetSum = 1
    res = True
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res

  
  def test_lc_run_3(self):
    root = [1,2,None,3,None,4,None,5]
    targetSum = 6
    res = False
    rootNode = bTree.create(root)
    assert prob.hasPathSum(rootNode, targetSum) == res