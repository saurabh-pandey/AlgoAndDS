import pytest

import dp.max_sum_partition as prob


class TestMaxSumPartition:
    def test_example1(self):
        arr = [1,15,7,9,2,5,10]
        k = 3
        res = 84
        assert prob.max_sum_partition(arr, k) == res
    
    def test_example2(self):
        arr = [1,4,1,5,7,3,6,1,9,9,3]
        k = 4
        res = 83
        assert prob.max_sum_partition(arr, k) == res
    
    def test_example3(self):
        arr = [1]
        k = 1
        res = 1
        assert prob.max_sum_partition(arr, k) == res
        
    def test_my1(self):
        arr = [1,2,3]
        k = 1
        res = 6
        assert prob.max_sum_partition(arr, k) == res
    
    def test_my2(self):
        arr = [1,2,3]
        k = 2
        res = 7
        assert prob.max_sum_partition(arr, k) == res
    
    def test_my3(self):
        arr = [1,2,3,4,5]
        k = 3
        res = 19
        assert prob.max_sum_partition(arr, k) == res
    