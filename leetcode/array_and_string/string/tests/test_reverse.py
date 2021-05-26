import pytest

import array_and_string.string.reverse as prob

class TestReverseString:
  def test_example1(self):
    s = ["h","e","l","l","o"]
    res = ["o","l","l","e","h"]
    prob.reverseString(s)
    assert s == res
  

  def test_example2(self):
    s = ["H","a","n","n","a","h"]
    res=  ["h","a","n","n","a","H"]
    prob.reverseString(s)
    assert s == res
  

  def test_empty(self):
    s = []
    res=  []
    prob.reverseString(s)
    assert s == res
  

  def test_size_1(self):
    s = ["a"]
    res=  ["a"]
    prob.reverseString(s)
    assert s == res