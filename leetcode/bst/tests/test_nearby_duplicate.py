import pytest

import bst.nearby_duplicate as prob

import random

class TestNearbyDuplicate:
    def test_example1(self):
        nums = [1,2,3,1]
        k = 3
        t = 0
        res = True
        assert prob.containsNearbyAlmostDuplicate(nums, k, t) == res
    

    def test_example2(self):
        nums = [1,0,1,1]
        k = 1
        t = 2
        res = True
        assert prob.containsNearbyAlmostDuplicate(nums, k, t) == res
    

    def test_example3(self):
        nums = [1,5,9,1,5,9]
        k = 2
        t = 3
        res = False
        assert prob.containsNearbyAlmostDuplicate(nums, k, t) == res
    

    def test_lc1(self):
        nums = [2147483647,-1,2147483647]
        k = 1
        t = 2147483647
        res = False
        assert prob.containsNearbyAlmostDuplicate(nums, k, t) == res
