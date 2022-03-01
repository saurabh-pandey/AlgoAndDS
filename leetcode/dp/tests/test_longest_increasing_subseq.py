import pytest

import dp.longest_increasing_subseq as prob

class TestLongestIncreasingSubsequence:
    def test_example1(self):
        nums = [10,9,2,5,3,7,101,18]
        res = 4
        assert prob.longest_inc_subseq(nums) == res
    
    def test_example2(self):
        nums = [0,1,0,3,2,3]
        res = 4
        assert prob.longest_inc_subseq(nums) == res
    
    def test_example3(self):
        nums = [7,7,7,7,7,7,7]
        res = 1
        assert prob.longest_inc_subseq(nums) == res
    
    def test_my1(self):
        nums = [1,2,3,4,5]
        res = 5
        assert prob.longest_inc_subseq(nums) == res
    
    def test_my2(self):
        nums = [7,8,9,1,2,3,4,5]
        res = 5
        assert prob.longest_inc_subseq(nums) == res
    
    def test_my2(self):
        nums = [1,7,2,8,3,9,4,10,5]
        res = 5
        assert prob.longest_inc_subseq(nums) == res
