import pytest

import parity_right_propagate_a1 as a1

solutions = {"attempt1": a1.right_propagate}

class TestRightPropagate:
    def test_example1(self):
        for attempt, solve in solutions.items():
            x = 0b01010000
            res = solve(x)
            expected = 0b01011111
            assert res == expected, attempt
