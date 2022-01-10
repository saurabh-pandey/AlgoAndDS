import pytest

import dp.maximum_subarray as prob

class TestMaximumSubarray:
    def test_example1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        res = 6
        assert prob.maxSubArray(nums) == res