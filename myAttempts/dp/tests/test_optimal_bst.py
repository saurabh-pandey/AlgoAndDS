import pytest

import dp.optimal_bst as prob


class TestOptimalBST:
    def test_example1(self):
        keys = [1,2,3,4]
        freq = [3,23,73,1]
        res = 136
        assert prob.optimal_bst_cost(keys, freq) == res
    
    def test_example2(self):
        keys = [1,2,3,4]
        freq = [1,34,33,32]
        res = 168
        assert prob.optimal_bst_cost(keys, freq) == res
    
    def test_example3(self):
        keys = [10,12]
        freq = [34,50]
        res = 118
        assert prob.optimal_bst_cost(keys, freq) == res
    
    def test_example4(self):
        keys = [10,12,20]
        freq = [34,8,50]
        res = 142
        assert prob.optimal_bst_cost(keys, freq) == res
    