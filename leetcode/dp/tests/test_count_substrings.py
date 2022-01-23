import pytest

import dp.count_substrings as prob

class TestCountSubstrings:
    def test_example1(self):
        s = "aba"
        t = "baba"
        res = 6
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_example2(self):
        s = "ab"
        t = "bb"
        res = 3
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_empty(self):
        s = ""
        t = ""
        res = 0
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_s_empty(self):
        s = "a"
        t = ""
        res = 0
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_t_empty(self):
        s = ""
        t = "a"
        res = 0
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_one_match(self):
        s = "a"
        t = "a"
        res = 0
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_all_match(self):
        s = "aaaaaa"
        t = "aaaaaa"
        res = 0
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_one_mismatch(self):
        s = "a"
        t = "b"
        res = 1
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res
    
    def test_two_mismatch(self):
        s = "aa"
        t = "bb"
        res = 4
        assert prob.countSubstring_bf(s, t) == res
        assert prob.countSubstring_o3(s, t) == res