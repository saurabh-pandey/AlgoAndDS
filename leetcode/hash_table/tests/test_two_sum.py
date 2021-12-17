import pytest

import hash_table.two_sum as prob

class TestTwoSum:
    def test_example1(self):
        nums = [2,7,11,15]
        target = 9
        res = [0,1]
        assert prob.twoSum(nums, target) == res
    
    def test_example2(self):
        nums = [3,2,4]
        target = 6
        res = [1,2]
        assert prob.twoSum(nums, target) == res
    
    def test_example3(self):
        nums = [3,3]
        target = 6
        res = [0,1]
        assert prob.twoSum(nums, target) == res