import pytest

import hash_table.four_sum as prob

class TestFourSum:
    def test_example1(self):
        nums1 = [1,2]
        nums2 = [-2,-1]
        nums3 = [-1,2]
        nums4 = [0,2]
        res = 2
        assert prob.fourSumCount(nums1, nums2, nums3, nums4) == res
    
    def test_example2(self):
        nums1 = [0]
        nums2 = [0]
        nums3 = [0]
        nums4 = [0]
        res = 1
        assert prob.fourSumCount(nums1, nums2, nums3, nums4) == res
    
    def test_my1(self):
        nums1 = [1,2]
        nums2 = [-2,-1]
        nums3 = [3,4]
        nums4 = [-4,-3]
        res = 6
        assert prob.fourSumCount(nums1, nums2, nums3, nums4) == res