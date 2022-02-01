import pytest

import dp.sort_by_power_val as prob

class TestSortByPowerValue:
    def test_example1(self):
        lo = 12
        hi = 15
        k = 2
        res = 13
        assert prob.getKth_bf(lo, hi, k) == res
    
    def test_example2(self):
        lo = 7
        hi = 11
        k = 4
        res = 7
        assert prob.getKth_bf(lo, hi, k) == res