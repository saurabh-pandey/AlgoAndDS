import pytest

import bst.operations as bst
import bst.lowest_common_ancestor as prob
from bst.node import Node


class TestLowestCommonAncestor:
    def test_example1(self):
        root = [6,2,8,0,4,7,9,None,None,3,5]
        p = 2
        q = 8
        res = 6
        rootNode = bst.create(root)
        lca = prob.lowestCommonAncestor(rootNode, Node(p), Node(q))
        assert lca.val == res
    

    def test_example2(self):
        root = [6,2,8,0,4,7,9,None,None,3,5]
        p = 2
        q = 4
        res = 2
        rootNode = bst.create(root)
        lca = prob.lowestCommonAncestor(rootNode, Node(p), Node(q))
        assert lca.val == res
    

    def test_example3(self):
        root = [2,1]
        p = 2
        q = 1
        res = 2
        rootNode = bst.create(root)
        lca = prob.lowestCommonAncestor(rootNode, Node(p), Node(q))
        assert lca.val == res
