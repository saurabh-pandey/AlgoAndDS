import pytest

import bst.operations as bst
import bst.bst_delete as prob

class TestBstDelete:
  def test_example1(self):
    root = [5,3,6,2,4,None,7]
    key = 3
    res = [5,4,6,2,None,None,7]
    rootNode = bst.create(root)
    print(bst.toList(rootNode))
    newRoot = prob.deleteNode(rootNode, key)
    # assert bst.toList(newRoot) == res
    print(bst.toList(newRoot))