import pytest

from bst.kth_largest import KthLargest

import random

class TestKthLargest:
    def test_example1(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        kthLargest.new_add(3)
        assert kthLargest.add(3) == 4
        # kthLargest.new_add(5)
        assert kthLargest.add(5) == 5
        assert kthLargest.add(10) == 5
        assert kthLargest.add(9) == 8
        assert kthLargest.add(4) == 8
    
    def test_my_example1(self):
        print()
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
        kthLargest = KthLargest(3, [])
        rounds = 20
        for i in range(rounds):
            n = random.randint(1, 20)
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
        print()
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