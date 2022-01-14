import pytest

import dp.all_full_binary_tree as prob

import bst.operations as bst

class TestAllPossibleFBT:
    def checkTrees(self, expected, output):
        for tree in output:
            treeList = bst.toList(tree)
            assert treeList in expected
    
    def test_example1(self):
        n = 7
        res = [[0,0,0,None,None,0,0,None,None,0,0],
               [0,0,0,None,None,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,None,None,None,None,0,0],
               [0,0,0,0,0,None,None,0,0]]
        allFBTs = prob.allPossibleFBT(n)
        self.checkTrees(res, allFBTs)
    
    def test_example2(self):
        n = 3
        res = [[0,0,0]]
        allFBTs = prob.allPossibleFBT(n)
        self.checkTrees(res, allFBTs)
    
    def test_single(self):
        n = 1
        res = [[0]]
        allFBTs = prob.allPossibleFBT(n)
        self.checkTrees(res, allFBTs)
    
    def test_two(self):
        n = 2
        res = []
        allFBTs = prob.allPossibleFBT(n)
        self.checkTrees(res, allFBTs)
