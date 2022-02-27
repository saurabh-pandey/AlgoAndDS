import pytest

import dp.house_robber as prob


class TestHouseRobber:
    def test_example1(self):
        nums = [1,2,3,1]
        res = 4
        assert prob.rob(nums) == res
    
    def test_example2(self):
        nums = [2,7,9,3,1]
        res = 12
        assert prob.rob(nums) == res