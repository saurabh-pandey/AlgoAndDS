import pytest

import binary_tree.build_from_in_post_order as prob
import binary_tree.operations as bTree

class TestBuildFromInAndPostOrder:
  def test_example_1(self):
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    res = [3,9,20,15,7]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res
  

  def test_example_2(self):
    inorder = [-1]
    postorder = [-1]
    res = [-1]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res
  

  def test_empty(self):
    inorder = []
    postorder = []
    res = []
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res
  

  def test_my_example_1(self):
    inorder = [2,1,3]
    postorder = [2,3,1]
    res = [1,2,3]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res
  

  def test_my_example_2(self):
    inorder = [3,2,1]
    postorder = [3,2,1]
    res = [1,2,3]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res
  

  def test_my_example_3(self):
    inorder = [1,2,3]
    postorder = [3,2,1]
    res = [1,2,3]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res