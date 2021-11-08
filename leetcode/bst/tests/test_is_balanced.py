import pytest

import bst.operations as bst
import bst.is_balanced as prob


class TestIsBalanced:
    def test_example1(self):
        root = [3,9,20,None,None,15,7]
        res = True
        rootNode = bst.create(root)
        assert prob.isBalanced(rootNode) == res
    
    def test_example2(self):
        root = [1,2,2,3,3,None,None,4,4]
        res = False
        rootNode = bst.create(root)
        assert prob.isBalanced(rootNode) == res
    
    def test_example3(self):
        root = []
        res = True
        rootNode = bst.create(root)
        assert prob.isBalanced(rootNode) == res
    
    def test_lc1(self):
        root = [1,2,2,3,None,None,3,4,None,None,4]
        res = False
        rootNode = bst.create(root)
        assert prob.isBalanced(rootNode) == res