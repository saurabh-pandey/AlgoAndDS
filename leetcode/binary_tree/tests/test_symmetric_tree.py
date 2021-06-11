import pytest

import binary_tree.symmetric_tree as prob
import binary_tree.operations as bTree

class TestSymmetricTree:
  def test_example1(self):
    root = [1,2,2,3,4,4,3]
    res = True
    rootNode = bTree.create(root)
    assert prob.isSymmetric(rootNode) == res
  

  def test_example2(self):
    root = [1,2,2,None,3,None,3]
    res = False
    rootNode = bTree.create(root)
    assert prob.isSymmetric(rootNode) == res