import pytest

import ch01_primitives.parity_right_propagate_a1 as a1

solutions = {"attempt1": a1.right_propagate}

class TestRightPropagate:
    def test_example1(self):
        for attempt, solve in solutions.items():
            x = 0b01010000
            res = solve(x)
            expected = 0b01011111
            assert res == expected, attempt
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            x = 0b1
            res = solve(x)
            expected = 0b1
            assert res == expected, attempt
    
    def test_example3(self):
        for attempt, solve in solutions.items():
            x = 0b0
            res = solve(x)
            expected = 0b0
            assert res == expected, attempt
    
    def test_example4(self):
        for attempt, solve in solutions.items():
            x = 0b1000
            res = solve(x)
            expected = 0b1111
            assert res == expected, attempt
