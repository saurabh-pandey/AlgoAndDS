import pytest

import hash_table.isomorphic_strings as prob

class TestIsomorphicStrings:
    def test_example1(self):
        s = "egg"
        t = "add"
        res = True
        assert prob.isIsomorphic(s, t) == res
    
    def test_example2(self):
        s = "foo"
        t = "bar"
        res = False
        assert prob.isIsomorphic(s, t) == res
    
    def test_example3(self):
        s = "paper"
        t = "title"
        res = True
        assert prob.isIsomorphic(s, t) == res
    
    def test_lc1(self):
        s = "badc"
        t = "baba"
        res = False
        assert prob.isIsomorphic(s, t) == res