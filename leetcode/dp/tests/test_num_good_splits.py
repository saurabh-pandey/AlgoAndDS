import pytest

import dp.num_good_splits as prob

class TestNumGoodSplits:
    def test_example1(self):
        s = "aacaba"
        res = 2
        assert prob.numSplits(s) == res
    
    def test_example2(self):
        s = "abcd"
        res = 1
        assert prob.numSplits(s) == res
    
    def test_one(self):
        s = "a"
        res = 0
        assert prob.numSplits(s) == res
    
    def test_two(self):
        s = "ab"
        res = 1
        assert prob.numSplits(s) == res