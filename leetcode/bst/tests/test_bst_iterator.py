import pytest

import bst.operations as bst
import bst.bst_iterator as it

class TestBstIterator:
  def test_example1(self):
    root = [7, 3, 15, None, None, 9, 20]
    rootNode = bst.create(root)

    bst_it = it.BSTIterator(rootNode)
    assert bst_it.next() == 3
    assert bst_it.hasNext() == True
    assert bst_it.next() == 7
    assert bst_it.hasNext() == True
    assert bst_it.next() == 9
    assert bst_it.hasNext() == True
    assert bst_it.next() == 15
    assert bst_it.hasNext() == True
    assert bst_it.next() == 20
    assert bst_it.hasNext() == False
    assert bst_it.next() == None
    assert bst_it.hasNext() == False