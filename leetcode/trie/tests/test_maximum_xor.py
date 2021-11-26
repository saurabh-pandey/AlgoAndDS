import pytest

import trie.maximum_xor as prob

class TestMaximumXor:
    def test_example1(self):
        nums = [3,10,5,25,2,8]
        res = 28
        # prob.findMaximumXOR(nums)
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