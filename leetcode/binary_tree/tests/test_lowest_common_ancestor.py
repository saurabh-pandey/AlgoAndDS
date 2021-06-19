import pytest

import binary_tree.lowest_common_ancestor as prob
import binary_tree.operations as bTree

class TestLowestCommonAncestor:
  def test_example_1(self):
    root = [3,5,1,6,2,0,8,None,None,7,4]
    p = 5
    q = 1
    res = 3
    rootNode = bTree.create(root)
    lcaNode = prob.lowestCommonAncestor(rootNode, bTree.Node(p), bTree.Node(q))
    assert lcaNode.val == res