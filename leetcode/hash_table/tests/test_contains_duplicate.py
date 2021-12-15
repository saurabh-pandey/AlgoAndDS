import pytest

import hash_table.contains_duplicate as prob

class TestContainsDuplicate:
    def test_example1(self):
        nums = [1,2,3,1]
        res = True
        assert prob.containsDuplicate(nums) == res
    
    def test_example2(self):
        nums = [1,2,3,4]
        res = False
        assert prob.containsDuplicate(nums) == res
    
    def test_example3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        res = True
        assert prob.containsDuplicate(nums) == res