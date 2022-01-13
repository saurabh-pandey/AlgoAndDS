import pytest

import dp.all_full_binary_tree as prob

import bst.operations as bst
# import binary_tree.operations as bst

class TestAllPossibleFBT:
    def checkTrees(expected, output):
        for tree in output:
            assert tree in expected

    def test_try(self):
        n = 7
        print()
        allFBTs = prob.allPossibleFBT(n)
        print(len(allFBTs))
        for root in allFBTs:
            print(bst.toList(root))
    
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
