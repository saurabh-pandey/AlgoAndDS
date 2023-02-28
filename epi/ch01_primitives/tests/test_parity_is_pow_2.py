import pytest

import parity_is_pow_2_a1 as a1

solutions = {"attempt1": a1.is_pow_2}

class TestIsPower2:
    def test_example1(self):
        for attempt, solve in solutions.items():
            x = 0b01000000
            res = solve(x)
            expected = True
            assert res == expected, attempt
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            x = 0b11000000
            res = solve(x)
            expected = False
            assert res == expected, attempt
