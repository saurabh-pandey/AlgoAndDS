import pytest

import array_and_string.string.reverse_words as prob

class TestReverseWords:
  def test_example1(self):
    s = "Let's take LeetCode contest"
    res = "s'teL ekat edoCteeL tsetnoc"
    assert prob.reverseWords(s) == res
    
  
  def test_example2(self):
    s = "God Ding"
    res = "doG gniD"
    assert prob.reverseWords(s) == res