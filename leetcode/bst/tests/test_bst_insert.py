import pytest

import bst.operations as bst
import bst.bst_insert as prob

class TestBstIterator:
  def test_example1(self):
    root = [4,2,7,1,3]
    val = 5
    res = [4,2,7,1,3,5]
    rootNode = bst.create(root)
    newRoot = prob.insertIntoBST(rootNode, val)
    assert bst.toList(newRoot) == res