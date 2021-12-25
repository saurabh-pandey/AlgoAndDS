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
    
    def test_empty(self):
        s = ""
        res = 0
        assert prob.lengthOfLongestSubstring(s) == res
    
    def test_my1(self):
        s = "abcbaac"
        res = 3
        assert prob.lengthOfLongestSubstring(s) == res
    
    def test_my2(self):
        s = "aaaabbbb"
        res = 2
        assert prob.lengthOfLongestSubstring(s) == res
    
    def test_my3(self):
        s = "aaaaaabcdeffffff"
        res = 6
        assert prob.lengthOfLongestSubstring(s) == res