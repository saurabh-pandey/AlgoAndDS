import pytest

import hash_table.longest_substring as prob

class TestLongestSubstring:
    def test_example1(self):
        s = "abcabcbb"
        res = 3
        assert prob.lengthOfLongestSubstring(s) == res
    
    def test_example2(self):
        s = "bbbbb"
        res = 1
        assert prob.lengthOfLongestSubstring(s) == res
    
    def test_example3(self):
        s = "pwwkew"
        res = 3
        assert prob.lengthOfLongestSubstring(s) == res