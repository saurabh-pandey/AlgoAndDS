import pytest

import hash_table.single_number as prob

class TestSingleNumber:
    def test_example1(self):
        nums = [2,2,1]
        res = 1
        assert prob.singleNumber(nums) == res
    
    def test_example2(self):
        nums = [4,1,2,1,2]
        res = 4
        assert prob.singleNumber(nums) == res
    
    def test_example3(self):
        nums = [1]
        res = 1
        assert prob.singleNumber(nums) == res