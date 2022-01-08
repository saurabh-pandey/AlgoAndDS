import pytest

import dp.min_cost_climb as prob


class TestMinClimbCost:
    def test_example1(self):
        cost = [10,15,20]
        res = 15
        assert prob.minCostClimbingStairs(cost) == res
    
    def test_example2(self):
        cost = [1,100,1,1,1,100,1,1,100,1]
        res = 6
        assert prob.minCostClimbingStairs(cost) == res