import pytest

import arrays.remove_duplicate_sorted_a1 as a1
import arrays.remove_duplicate_sorted_a2 as a2

# solutions = {"attempt1": a1.removeElement, "attempt2": a2.remove_element}
solutions = {"attempt1_v1": a1.removeDuplicatesOverwrite,
             "attempt1_v2": a1.removeDuplicatesRetainAll}

class TestRemoveDuplicateSorted:
    def test_example1(self):
        for attempt, solve in solutions.items():
            nums = [1,1,2]
            newLen = solve(nums)
            assert newLen == 2, attempt
            excepted = [1,2]
            assert nums[:newLen] == excepted, attempt
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            nums = [0,0,1,1,1,2,2,3,3,4]
            newLen = solve(nums)
            assert newLen == 5, attempt
            excepted = [0,1,2,3,4]
            assert nums[:newLen] == excepted, attempt
    
    def test_empty(self):
        for attempt, solve in solutions.items():
            nums = []
            newLen = solve(nums)
            assert newLen == 0, attempt
            excepted = []
            assert nums == excepted, attempt
    
    def test_size_1(self):
        for attempt, solve in solutions.items():
            nums = [1]
            newLen = solve(nums)
            assert newLen == 1, attempt
            excepted = [1]
            assert nums[:newLen] == excepted, attempt
    
    def test_all_duplicate(self):
        for attempt, solve in solutions.items():
            nums = [1,1,1,1]
            newLen = solve(nums)
            assert newLen == 1, attempt
            excepted = [1]
            assert nums[:newLen] == excepted, attempt
