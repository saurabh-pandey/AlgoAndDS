import pytest

import dp.max_sum_partition as prob


class TestMaxSumPartition:
    def test_example1(self):
        arr = [1,15,7,9,2,5,10]
        k = 3
        res = 84
        assert prob.max_sum_partition(arr, k) == res
        print(prob.max_sum_partition([1], 1))
        print(prob.max_sum_partition([1,2,3], 1))
        print(prob.max_sum_partition([1,2,3], 2))
        print(prob.max_sum_partition([1,2,3,4,5], 3))