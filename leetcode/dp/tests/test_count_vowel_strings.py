import pytest

import dp.count_vowel_strings as prob

class TestCountVowelStrings:
    def test_example1(self):
        n = 1
        res = 5
        assert prob.countVowelStrings(n) == res
    
    def test_example2(self):
        n = 2
        res = 15
        assert prob.countVowelStrings(n) == res
    
    def test_example3(self):
        n = 33
        res = 66045
        assert prob.countVowelStrings(n) == res
    
    def test_three(self):
        n = 3
        res = 35
        assert prob.countVowelStrings(n) == res