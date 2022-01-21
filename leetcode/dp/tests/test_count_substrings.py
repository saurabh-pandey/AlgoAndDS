import pytest

import dp.count_substrings as prob

class TestCountSubstrings:
    def test_example1(self):
        s = "aba"
        t = "baba"
        res = 6
        assert prob.countSubstring(s, t) == res