import pytest

import ch01_primitives.parity_mod_pow_2_a1 as a1

solutions = {"attempt1": a1.mod_pow_2}

class TestModPower2:
    def test_example1(self):
        for attempt, solve in solutions.items():
            x = 77
            power = 6 # 2^6 = 64
            res = solve(x, power)
            expected = 13
            assert res == expected, attempt
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            x = 64
            power = 6 # 2^6 = 64
            res = solve(x, power)
            expected = 0
            assert res == expected, attempt
    
    def test_example3(self):
        for attempt, solve in solutions.items():
            x = 3
            power = 1 # 2^1 = 2
            res = solve(x, power)
            expected = 1
            assert res == expected, attempt
    
    def test_example4(self):
        for attempt, solve in solutions.items():
            x = 77
            power = 2 # 2^2 = 4
            res = solve(x, power)
            expected = 1
            assert res == expected, attempt
