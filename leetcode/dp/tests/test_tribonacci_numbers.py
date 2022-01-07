import pytest

import dp.tribonacci_numbers as prob

class TestTribonacciNumbers:
    def test_example1(self):
        n = 4
        res = 4
        assert prob.tribonacci(n) == res
    
    def test_example2(self):
        n = 25
        res = 1389537
        assert prob.tribonacci(n) == res
    
    def test_my1(self):
        n = 0
        res = 0
        assert prob.tribonacci(n) == res