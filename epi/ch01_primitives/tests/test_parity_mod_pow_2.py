import pytest

import parity_mod_pow_2_a1 as a1

solutions = {"attempt1": a1.mod_pow_2}

class TestModPower2:
    def test_example1(self):
        for attempt, solve in solutions.items():
            x = 77
            power = 6 # 2^6 = 64
            res = solve(x, power)
            expected = 13
            assert res == expected, attempt
