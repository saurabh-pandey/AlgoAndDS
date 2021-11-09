import pytest

import bst.operations as bst
import bst.sorted_arr_to_bst as prob

class TestSortedArrToBst:
    def test_example1(self):
        nums = [-10,-3,0,5,9]
        res = [0,-3,9,-10,None,5]
        root = prob.sortedArrayToBST(nums)
        assert bst.toList(root) == res
    
    def test_example2(self):
        nums = [1, 3]
        res = [3, 1]
        root = prob.sortedArrayToBST(nums)
        assert bst.toList(root) == res
    
    def test_empty(self):
        nums = []
        res = []
        root = prob.sortedArrayToBST(nums)
        assert bst.toList(root) == res
    
    def test_my1(self):
        nums = [1,2,3,4,5,6,7]
        res = [4,2,6,1,3,5,7]
        root = prob.sortedArrayToBST(nums)
        assert bst.toList(root) == res