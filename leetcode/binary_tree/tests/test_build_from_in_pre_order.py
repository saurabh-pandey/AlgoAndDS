import pytest

import binary_tree.build_from_in_pre_order as prob
import binary_tree.operations as bTree

class TestBuildFromInAndPreOrder:
  def test_example_1(self):
    inorder = [9,3,15,20,7]
    preorder = [3,9,20,15,7]
    res = [3,9,20,15,7]
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res
  

  def test_example_2(self):
    inorder = [-1]
    preorder = [-1]
    res = [-1]
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res
  

  def test_empty(self):
    inorder = []
    preorder = []
    res = []
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res
  

  # def test_my_example_1(self):
    inorder = [2,1,3]
    preorder = [1,2,3]
    res = [1,2,3]
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res
  

  def test_my_example_2(self):
    inorder = [3,2,1]
    preorder = [1,2,3]
    res = [1,2,3]
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res
  

  def test_my_example_3(self):
    inorder = [1,2,3]
    preorder = [1,2,3]
    res = [1,2,3]
    root = prob.buildTree(inorder, preorder)
    assert bTree.toList(root) == res