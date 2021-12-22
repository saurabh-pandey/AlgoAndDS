import pytest

from bst.node import Node
import bst.operations as bTree

import hash_table.find_duplicate_subtrees as prob

class TestFindDupicateSubtrees:
    def test_example1(self):
        root = [1,2,3,4,None,2,4,None,None,4]
        res = [[2,4],[4]]
        rootNode = bTree.create(root)
        rt_list = bTree.toList(rootNode)
        # print(rt_list)
        # key = ",".join(str(n) for n in rt_list)
        # for n in rt_list:
        #     if n is not None:
        #         key += str(n)
        #     else:
        #         key += "N"
        #     key += ","
        # print(key)
        
        dup_trees = prob.findDuplicateSubtrees(rootNode)
        # print(dup_trees)
        for dup_root in dup_trees:
            tree_list = bTree.toList(dup_root)
            # print(tree_list)
            assert tree_list in res
    
    def test_example2(self):
        root = [2,1,1]
        res = [[1]]
        rootNode = bTree.create(root)        
        dup_trees = prob.findDuplicateSubtrees(rootNode)
        for dup_root in dup_trees:
            tree_list = bTree.toList(dup_root)
            # print(tree_list)
            assert tree_list in res
    
    def test_example3(self):
        root = [2,2,2,3,None,3,None]
        res = [[2,3],[3]]
        rootNode = bTree.create(root)        
        dup_trees = prob.findDuplicateSubtrees(rootNode)
        for dup_root in dup_trees:
            tree_list = bTree.toList(dup_root)
            # print(tree_list)
            assert tree_list in res
