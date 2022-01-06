import pytest

import dp.divisor_game as prob


class TestDivisorGame:
    def test_example1(self):
        n = 2
        res = True
        assert prob.divisorGame(n) == res
    
    def test_example2(self):
        n = 3
        res = False
        assert prob.divisorGame(n) == res
    
    def test_my1(self):
        startN = 4
        endN = 10
        res = [True, False, True, False, True, False, True]
        count = 0
        for i in range(startN, endN):
            assert prob.divisorGame(i) == res[count]
            count += 1