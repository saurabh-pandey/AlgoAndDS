import pytest

import hash_table.top_k_frequent as prob

class TestTopK_Frequent:
    def test_example1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        res = [1,2]
        assert prob.topKFrequent(nums, k) == res
    
    def test_example2(self):
        nums = [1]
        k = 1
        res = [1]
        assert prob.topKFrequent(nums, k) == res