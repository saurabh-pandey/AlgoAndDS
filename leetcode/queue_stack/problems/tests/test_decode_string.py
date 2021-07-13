import pytest

import queue_stack.problems.decode_string as prob

class TestDecodeString:
  def test_my_example1(self):
    s = "3[a]"
    res = "aaa"
    assert prob.decodeString(s) == res
  

  def test_my_example2(self):
    s = "a"
    res = "a"
    assert prob.decodeString(s) == res
  

  def test_empty(self):
    s = ""
    res = ""
    assert prob.decodeString(s) == res
  

  def test_example1(self):
    s = "3[a]2[bc]"
    res = "aaabcbc"
    assert prob.decodeString(s) == res
  

  def test_example2(self):
    s = "3[a2[c]]"
    res = "accaccacc"
    assert prob.decodeString(s) == res
  

  def test_example3(self):
    s = "2[abc]3[cd]ef"
    res = "abcabccdcdcdef"
    assert prob.decodeString(s) == res
  

  def test_example4(self):
    s = "abc3[cd]xyz"
    res = "abccdcdcdxyz"
    assert prob.decodeString(s) == res
  

  def test_my_example3(self):
    s = "12[ab]"
    res = 12*"ab"
    assert prob.decodeString(s) == res
  

  def test_my_example3(self):
    s = "ab2[cd3[ef]gh]ij"
    res = "ab" + 2*"cdefefefgh" + "ij"
    assert prob.decodeString(s) == res