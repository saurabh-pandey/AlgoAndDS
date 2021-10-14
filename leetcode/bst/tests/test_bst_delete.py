import pytest

import bst.operations as bst
import bst.bst_delete as prob

class TestBstDelete:
    def test_example1(self):
        root = [5,3,6,2,4,None,7]
        key = 3
        res = [5,4,6,2,None,None,7]
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
    
    def test_example2(self):
        root = [5,3,6,2,4,None,7]
        key = 0
        res = [5,3,6,2,4,None,7]
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
    
    def test_example3(self):
        root = []
        key = 0
        res = []
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
    
    def test_lc1(self):
        root = [5,3,6,2,4,None,7]
        key = 7
        res = [5,3,6,2,4]
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
    
    def test_lc2(self):
        root = [4,None,7,6,8,5,None,None,9]
        key = 7
        res = [4,None,8,6,9,5]
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
    
    def test_lc3(self):
        root = [3,2,4,1]
        key = 3
        res = [4,2,None,1]
        rootNode = bst.create(root)
        newRoot = prob.deleteNode(rootNode, key)
        assert bst.toList(newRoot) == res
