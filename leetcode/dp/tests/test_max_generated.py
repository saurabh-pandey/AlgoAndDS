import pytest

import dp.max_generated as prob

class TestMaxGenerated:
    def test_example1(self):
        n = 7
        res = 3
        assert prob.getMaximumGenerated(n) == res
    
    def test_example2(self):
        n = 2
        res = 1
        assert prob.getMaximumGenerated(n) == res
    
    def test_example3(self):
        n = 3
        res = 2
        assert prob.getMaximumGenerated(n) == res
    
    def test_zero(self):
        n = 0
        res = 0
        assert prob.getMaximumGenerated(n) == res
    
    def test_one(self):
        n = 1
        res = 1
        assert prob.getMaximumGenerated(n) == res