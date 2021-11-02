import pytest

from bst.kth_largest import KthLargest

import random
import bisect

# Array based kth largest for comparison
class KthLargestAsArray:
    def __init__(self, k, nums) -> None:
        self.k = k
        self.nums = nums
        self.nums.sort()
    
    def _nums(self):
        return self.nums
    
    def find_kth(self):
        if self.k > len(self.nums):
            return None
        else:
            return self.nums[-self.k]
    
    def add(self, val):
        kth_val = self.find_kth()
        if kth_val and kth_val > val:
            return kth_val
        else:
            it = bisect.bisect_left(self.nums, val)
            self.nums.insert(it, val)
            return self.find_kth()


# Tests
class TestKthLargest:
    def test_example1(self):
        kthLargestAsArr = KthLargestAsArray(3, [4, 5, 8, 2])
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        assert kthLargestAsArr.add(3) == kthLargest.add(3)
        assert kthLargestAsArr.add(5) == kthLargest.add(5)
        assert kthLargestAsArr.add(10) == kthLargest.add(10)
        assert kthLargestAsArr.add(9) == kthLargest.add(9)
        assert kthLargestAsArr.add(4) == kthLargest.add(4)
    

    def test_my_example1(self):
        k = 3
        kthLargest = KthLargest(k, [])
        kthLargestAsArr = KthLargestAsArray(k, [])
        all_nums = [6,4,10,8,5,9,11,3,7]
        for n in all_nums:
            assert kthLargestAsArr.add(n) == kthLargest.add(n)
    
    
    def test_decreasing(self):
        k = 2
        max_val = 1000
        kthLargestAsArr = KthLargestAsArray(k, [])
        kthLargest = KthLargest(k, [])
        for i in range(k - 1):
            assert kthLargestAsArr.add(max_val - i) == kthLargest.add(max_val - i)
        for n in range(max_val - k + 1, -1, -1):
            assert kthLargestAsArr.add(n) == kthLargest.add(n)
    
    def test_increasing(self):
        k = 4
        max_val = 100
        kthLargestAsArr = KthLargestAsArray(k, [])
        kthLargest = KthLargest(k, [])
        for i in range(k - 1):
            assert kthLargestAsArr.add(i) == kthLargest.add(i)
        for n in range(k - 1, max_val + 1):
            assert kthLargestAsArr.add(n) == kthLargest.add(n)

    
    def test_random(self):
        k = 6
        kthLargest = KthLargest(k, [])
        kthLargestAsArr = KthLargestAsArray(k, [])
        rounds = 40
        for i in range(rounds):
            n = random.randint(1, 40)
            arr_res = kthLargestAsArr.add(n)
            bst_res = kthLargest.add(n)
            assert arr_res == bst_res
    
    
    def test_duplicate(self):
        k = 3
        kthLargestAsArr = KthLargestAsArray(k, [])
        kthLargest = KthLargest(k, [])
        all_nums = [3, 17, 17, 15]
        for n in all_nums:
            bst_res = kthLargest.add(n)
            arr_res = kthLargestAsArr.add(n)
            assert arr_res == bst_res
    

    def test_large(self):
        k = 9999
        kthLargestAsArr = KthLargestAsArray(k, [])
        kthLargest = KthLargest(k, [])
        for i in range(20000):
            n = random.randint(-5000, 5000)
            bst_res = kthLargest.add(n)
            arr_res = kthLargestAsArr.add(n)
            assert arr_res == bst_res
    