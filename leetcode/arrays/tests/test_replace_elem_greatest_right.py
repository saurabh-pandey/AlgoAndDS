import pytest

import arrays.replace_elem_greatest_right_a1 as a1
import arrays.replace_elem_greatest_right_a2 as a2

solutions = {"attempt1": a1.replaceElements,
             "attempt2": a2.replace_elements}

class TestReplaceElemGreatestRight:
    def test_example1(self):
        for attempt, solve in solutions.items():
            arr = [17,18,5,4,6,1]
            expected = [18,6,6,6,1,-1]
            assert solve(arr) == expected, attempt
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            arr = [400]
            expected = [-1]
            assert solve(arr) == expected, attempt
    
    def test_empty(self):
        for attempt, solve in solutions.items():
            arr = []
            expected = []
            assert solve(arr) == expected, attempt
    
    def test_max_last(self):
        for attempt, solve in solutions.items():
            arr = [0,1,2,3,4,5,6]
            expected = [6,6,6,6,6,6,-1]
            assert solve(arr) == expected, attempt
    
    def test_descending(self):
        for attempt, solve in solutions.items():
            arr = [9,8,7,6,5,4,3,2,1]
            expected = [8,7,6,5,4,3,2,1,-1]
            assert solve(arr) == expected, attempt
