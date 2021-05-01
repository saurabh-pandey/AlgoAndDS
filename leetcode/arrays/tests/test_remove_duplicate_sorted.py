import pytest

import arrays.remove_duplicate_sorted as prob

class TestRemoveDuplicateSorted:
    def test_example1(self):
        nums = [1,1,2]
        newLen = prob.removeDuplicates(nums)
        assert newLen == 2
        excepted = [1,2]
        assert nums[:newLen] == excepted
    
    def test_example2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        newLen = prob.removeDuplicates(nums)
        assert newLen == 5
        excepted = [0,1,2,3,4]
        assert nums[:newLen] == excepted
    
    def test_empty(self):
        nums = []
        newLen = prob.removeDuplicates(nums)
        assert newLen == 0
        excepted = []
        assert nums == excepted
    
    def test_size_1(self):
        nums = [1]
        newLen = prob.removeDuplicates(nums)
        assert newLen == 1
        excepted = [1]
        assert nums[:newLen] == excepted
    
    def test_all_duplicate(self):
        nums = [1,1,1,1]
        newLen = prob.removeDuplicates(nums)
        assert newLen == 1
        excepted = [1]
        assert nums[:newLen] == excepted