import pytest

import recursion_2.letter_combinations as prob

class TestLetterCombinations:
  def test_example1(self):
    digits = "23"
    res =  {"ad","ae","af","bd","be","bf","cd","ce","cf"}
    assert res == set(prob.letterCombinations(digits))
  

  def test_example2(self):
    digits = ""
    res =  set()
    assert res == set(prob.letterCombinations(digits))
  

  def test_example3(self):
    digits = "2"
    res =  {"a","b","c"}
    assert res == set(prob.letterCombinations(digits))