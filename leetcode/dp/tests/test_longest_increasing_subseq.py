import pytest

import dp.longest_increasing_subseq as prob

class TestLongestIncreasingSubsequence:
    def test_example1(self):
        nums = [10,9,2,5,3,7,101,18]
        res = 4
        assert prob.longest_inc_subseq(nums) == res