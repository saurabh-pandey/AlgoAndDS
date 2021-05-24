import pytest

import array_and_string.string.str_str as prob

class TestStrStr:
  def test_example1(self):
    haystack = "hello"
    needle = "ll"
    assert prob.strStr(haystack, needle) == 2
  

  def test_example2(self):
    haystack = "aaaaa"
    needle = "bba"
    assert prob.strStr(haystack, needle) == -1
  

  def test_example3(self):
    haystack = ""
    needle = ""
    assert prob.strStr(haystack, needle) == 0
  

  def test_my_example1(self):
    haystack = "abcdef"
    needle = ""
    assert prob.strStr(haystack, needle) == 0
  

  def test_my_example1(self):
    haystack = ""
    needle = "abc"
    assert prob.strStr(haystack, needle) == -1
  

  def test_my_example2(self):
    haystack = "aabbcccddbbaaaeefgh"
    needle = "aaa"
    assert prob.strStr(haystack, needle) == 11