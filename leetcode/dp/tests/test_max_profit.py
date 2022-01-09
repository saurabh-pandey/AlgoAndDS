import pytest

import dp.max_profit as prob

class TestMaxProfit:
    def test_example1(self):
        prices = [7,1,5,3,6,4]
        res = 5
        assert prob.maxProfit(prices) == res
    
    def test_example2(self):
        prices = [7,6,4,3,1]
        res = 0
        assert prob.maxProfit(prices) == res
    
    def test_single(self):
        prices = [5]
        res = 0
        assert prob.maxProfit(prices) == res
    
    def test_same(self):
        prices = [2,2,2,2,2,2]
        res = 0
        assert prob.maxProfit(prices) == res
    
    def test_sorted(self):
        prices = [1,2,3,4,5,6,7]
        res = 6
        assert prob.maxProfit(prices) == res
    
    def test_my1(self):
        prices = [7,2,5,4,1,3,6,2,8]
        res = 7
        assert prob.maxProfit(prices) == res