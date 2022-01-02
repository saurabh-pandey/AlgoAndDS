import pytest

import dp.count_bits as prob

class TestCountBits:
    def test_example1(self):
        n = 2
        res = [0,1,1]
        assert prob.countBits(n) == res
    
    def test_example2(self):
        n = 5
        res = [0,1,1,2,1,2]
        assert prob.countBits(n) == res
    
    def test_my1(self):
        n = 0
        res = [0]
        assert prob.countBits(n) == res