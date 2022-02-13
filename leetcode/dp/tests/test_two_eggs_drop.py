import pytest

import dp.two_eggs_drop as prob

class TestTwoEggsDrop:
    def test_example1(self):
        n = 2
        res = 2
        assert prob.two_eggs_drop(n) == res
    
    def test_example2(self):
        n = 100
        res = 14
        assert prob.two_eggs_drop(n) == res
    