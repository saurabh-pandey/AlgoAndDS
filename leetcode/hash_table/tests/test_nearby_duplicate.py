import pytest

import hash_table.nearby_duplicate as prob

class TestNearbyDuplicate:
    def test_example1(self):
        nums = [1,2,3,1]
        k = 3
        res = True
        assert prob.containsNearbyDuplicate(nums, k) == res
    
    def test_example2(self):
        nums = [1,0,1,1]
        k = 1
        res = True
        assert prob.containsNearbyDuplicate(nums, k) == res
    
    def test_example3(self):
        nums = [1,2,3,1,2,3]
        k = 2
        res = False
        assert prob.containsNearbyDuplicate(nums, k) == res