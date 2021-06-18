import pytest

import binary_tree.next_right_pointer as prob
import binary_tree.operations as bTree

def getNextRightList(root):
  nextRightList = []
  node = root
  while node is not None:
    nextRightList.append(node.val)

class TestNextRightPointer:
  def test_example1(self):
    root = [1,2,3,4,5,6,7]
    rootNode = bTree.create(root)
    res = [1,None,2,3,None,4,5,6,7,None]
    newRootNode = prob.connect(root)
