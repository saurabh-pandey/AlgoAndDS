import pytest

import random

import trie.maximum_xor as prob


class TestMaximumXor:
    def test_example1(self):
        nums = [3,10,5,25,2,8]
        res = 28
        assert prob.findMaximumXOR(nums) == res
    
    def test_example2(self):
        nums = [0]
        res = 0
        assert prob.findMaximumXOR(nums) == res
    
    def test_example3(self):
        nums = [2,4]
        res = 6
        assert prob.findMaximumXOR(nums) == res
    
    def test_example4(self):
        nums = [8,10,2]
        res = 10
        assert prob.findMaximumXOR(nums) == res
    
    def test_example5(self):
        nums = [14,70,53,83,49,91,36,80,92,51,66,70]
        res = 127
        assert prob.findMaximumXOR(nums) == res
    
    def test_random(self):
        sizes = [10, 50, 100, 500, 1000, 5000, 10000]
        for sz in sizes:
            print("\nTest size = ", sz)
            nums = [random.randint(0, sz) for _ in range(sz)]
            print("Testing Brute-force")
            res_bf = prob.findMaximumXOR_bf(nums)
            print("Brute-force = ", res_bf)
            print("Testing Trie")
            res_trie = prob.findMaximumXOR(nums)
            print("Trie = ", res_trie)
            assert res_bf == res_trie
    
    def test_lc1(self):
        nums = [10,23,20,18,28]
        res = 30
        assert prob.findMaximumXOR(nums) == res