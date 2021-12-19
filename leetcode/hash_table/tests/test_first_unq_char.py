import pytest

import hash_table.first_unq_char as prob

class TestFirstUniqueChar:
    def test_example1(self):
        s = "leetcode"
        res = 0
        assert prob.firstUniqChar(s) == res
    
    def test_example2(self):
        s = "loveleetcode"
        res = 2
        assert prob.firstUniqChar(s) == res
    
    def test_example3(self):
        s = "aabb"
        res = -1
        assert prob.firstUniqChar(s) == res
    
    def test_empty(self):
        s = ""
        res = -1
        assert prob.firstUniqChar(s) == res
    
    def test_single(self):
        s = "a"
        res = 0
        assert prob.firstUniqChar(s) == res