import pytest

from bst.kth_largest import KthLargest

import random

import bisect

import pdb

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


class TestKthLargest:
    def test_example1(self):
        kthLargestAsArr = KthLargestAsArray(3, [4, 5, 8, 2])
        assert kthLargestAsArr.add(3) == 4
        assert kthLargestAsArr.add(5) == 5
        assert kthLargestAsArr.add(10) == 5
        assert kthLargestAsArr.add(9) == 8
        assert kthLargestAsArr.add(4) == 8
    
    def test_decreasing(self):
        k = 2
        max_val = 1000
        kthLargestAsArr = KthLargestAsArray(k, [])
        for i in range(k - 1):
            assert kthLargestAsArr.add(max_val - i) == None
        for n in range(max_val - k + 1, -1, -1):
            assert kthLargestAsArr.add(n) == max_val - k + 1
    
    def test_increasing(self):
        k = 4
        max_val = 1000
        kthLargestAsArr = KthLargestAsArray(k, [])
        for i in range(k - 1):
            assert kthLargestAsArr.add(i) == None
        for n in range(k - 1, max_val + 1):
            assert kthLargestAsArr.add(n) == n - k + 1
    
    def test_my_example1(self):
        kthLargest = KthLargest(3, [])
        kthLargest.new_add(6)
        kthLargest.new_add(4)
        kthLargest.new_add(10)
        kthLargest.new_add(8)
        kthLargest.new_add(5)
        kthLargest.new_add(9)
        kthLargest.new_add(11)
        kthLargest.new_add(3)
        kthLargest.new_add(7)
        # print(kthLargest.toList())
    
    def test_my_example2(self):
        print()
        kthLargest = KthLargest(3, [])
        all_nums = [6,4,10,8,5,9,11,3,7]
        for n in all_nums:
            add_res = kthLargest.add(n)
            new_add_res = kthLargest.new_add(n)
            if add_res == new_add_res:
                print(f"Passing for n = {n}, res = {new_add_res}")
            else:
                print(f"Failed for n = {n}, new_add_res = {new_add_res}, add_res = {add_res}")
    
    def test_my_example3(self):
        print()
        kthLargest = KthLargest(6, [])
        rounds = 40
        for i in range(rounds):
            n = random.randint(1, 40)
            add_res = kthLargest.add(n)
            new_add_res = kthLargest.new_add(n)
            if add_res == new_add_res:
                print(f"Passing for n = {n}, res = {new_add_res}")
            else:
                print(f"Failed for n = {n}, new_add_res = {new_add_res}, add_res = {add_res}")
                print(kthLargest._nums())
                print(kthLargest.toList())
                break
    
    def test_my_example4(self):
        kthLargest = KthLargest(3, [])
        all_nums = [3, 17, 17, 15]
        # all_nums = [3, 17, 15, 17] # This works
        # all_nums = [3, 15, 17, 17] # This also works
        # all_nums = [17, 17, 3, 15] # But this doesn't
        for n in all_nums:
            add_res = kthLargest.add(n)
            new_add_res = kthLargest.new_add(n)
            if add_res == new_add_res:
                print(f"Passing for n = {n}, res = {new_add_res}")
            else:
                print(f"Failed for n = {n}, new_add_res = {new_add_res}, add_res = {add_res}")
                print(kthLargest._nums())
                print(kthLargest.toList())
                break
    
    def test_reverse(self):
        kthLargest = KthLargest(3, [])
        # all_nums = range(20, 0, -1)
        # all_nums = [3, 17, 15, 17] # This works
        # all_nums = [3, 15, 17, 17] # This also works
        # all_nums = [17, 17, 3, 15] # But this doesn't
        for n in range(20, 0, -1):
            add_res = kthLargest.add(n)
            new_add_res = kthLargest.new_add(n)
            # print(kthLargest.toList())
            if add_res == new_add_res:
                print(f"Passing for n = {n}, res = {new_add_res}")
            else:
                print(f"Failed for n = {n}, new_add_res = {new_add_res}, add_res = {add_res}")
                print(kthLargest._nums())
                print(kthLargest.toList())
                break
    

    def test_large(self):
        kthLargest = KthLargest(9999, [])
        # all_nums = range(20, 0, -1)
        # all_nums = [3, 17, 15, 17] # This works
        # all_nums = [3, 15, 17, 17] # This also works
        # all_nums = [17, 17, 3, 15] # But this doesn't
        for i in range(20000):
            n = random.randint(-5000, 5000)
            add_res = kthLargest.add(n)
            new_add_res = kthLargest.new_add(n)
            # print(kthLargest.toList())
            if add_res != new_add_res:
                print(f"Failed for n = {n}, new_add_res = {new_add_res}, add_res = {add_res}")
                print(kthLargest._nums())
                print(kthLargest.toList())
                break