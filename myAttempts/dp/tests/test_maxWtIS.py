import pytest

import dp.maxWtIS as prob

class TestMaxWtIS:
    def test_example1(self):
        nums = [1,4,5,4]
        res = [4,4]
        assert prob.maxWtIS(nums) == res
    
    def test_example2(self):
        nums = [1,4,8,4]
        res = [8,1]
        assert prob.maxWtIS(nums) == res
    
    def test_empty(self):
        nums = []
        res = []
        assert prob.maxWtIS(nums) == res
    
    def test_example3(self):
        nums = [1,2,3,4,5,6]
        res = [6,4,2]
        assert prob.maxWtIS(nums) == res
    
    def test_example4(self):
        nums = [1,2,3,4,5,6,7]
        res = [7,5,3,1]
        assert prob.maxWtIS(nums) == res