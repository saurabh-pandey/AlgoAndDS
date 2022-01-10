import pytest

import dp.is_subsequence as prob

class TestIsSubsequence:
    def test_example1(self):
        s = "abc"
        t = "ahbgdc"
        res = True
        assert prob.isSubsequence(s, t) == res
    
    def test_example2(self):
        s = "axc"
        t = "ahbgdc"
        res = False
        assert prob.isSubsequence(s, t) == res
    
    def test_both_empty(self):
        s = ""
        t = ""
        res = True
        assert prob.isSubsequence(s, t) == res
    
    def test_s_empty(self):
        s = ""
        t = "abc"
        res = True
        assert prob.isSubsequence(s, t) == res
    
    def test_t_empty(self):
        s = "a"
        t = ""
        res = False
        assert prob.isSubsequence(s, t) == res