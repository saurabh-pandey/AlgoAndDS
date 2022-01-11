import pytest

import dp.maximum_subarray as prob

class TestMaximumSubarray:
    def test_example1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        res = 6
        assert prob.maxSubArray(nums) == res
    
    def test_example2(self):
        nums = [1]
        res = 1
        assert prob.maxSubArray(nums) == res
    
    def test_example3(self):
        nums = [5,4,-1,7,8]
        res = 23
        assert prob.maxSubArray(nums) == res
    
    def test_all_neg_decreasing(self):
        nums = [-1,-2,-3,-4,-5]
        res = -1
        assert prob.maxSubArray(nums) == res
    
    def test_all_neg_increasing(self):
        nums = [-5,-4,-3,-2,-1]
        res = -1
        assert prob.maxSubArray(nums) == res
    
    def test_all_zero(self):
        nums = [0,0,0,0,0]
        res = 0
        assert prob.maxSubArray(nums) == res
    
    def test_all_pos_increasing(self):
        nums = [1,2,3,4,5]
        res = 15
        assert prob.maxSubArray(nums) == res
    
    def test_all_pos_decreasing(self):
        nums = [5,4,3,2,1]
        res = 15
        assert prob.maxSubArray(nums) == res
    
    def test_lc1(self):
        nums = [8,-19,5,-4,20]
        res = 21
        assert prob.maxSubArray(nums) == res
    
    def test_lc2(self):
        nums = [-2,1]
        res = 1
        assert prob.maxSubArray(nums) == res