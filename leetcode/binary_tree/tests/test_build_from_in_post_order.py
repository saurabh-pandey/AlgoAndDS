import pytest

import binary_tree.build_from_in_post_order as prob
import binary_tree.operations as bTree

class TestBuildFromInAndPostOrder:
  def test_example_1(self):
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    res = [3,9,20,None,None,15,7]
    root = prob.buildTree(inorder, postorder)
    assert bTree.toList(root) == res