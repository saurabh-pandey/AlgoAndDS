import pytest

import array_and_string.string.reverse_sentence as prob

class TestReverseSentence:
  def test_example1(self):
    s = "the sky is blue"
    result = "blue is sky the"
    assert prob.reverseWords(s) == result
  

  def test_example2(self):
    s = "  hello world  "
    result = "world hello"
    assert prob.reverseWords(s) == result
  

  def test_example3(self):
    s = "a good   example"
    result = "example good a"
    assert prob.reverseWords(s) == result
  

  def test_example4(self):
    s = "  Bob    Loves  Alice   "
    result = "Alice Loves Bob"
    assert prob.reverseWords(s) == result
  

  def test_example5(self):
    s = "Alice does not even like bob"
    result = "bob like even not does Alice"
    assert prob.reverseWords(s) == result
  

  def test_empty(self):
    s = ""
    result = ""
    assert prob.reverseWords(s) == result
  
  
  def test_all_space(self):
    s = "   "
    result = ""
    assert prob.reverseWords(s) == result
  

  def test_single_word(self):
    s = "one"
    result = "one"
    assert prob.reverseWords(s) == result
  

  def test_single_word_w_space(self):
    s = " one "
    result = "one"
    assert prob.reverseWords(s) == result
  

  def test_single_char(self):
    s = "s"
    result = "s"
    assert prob.reverseWords(s) == result
  

  def test_single_char_w_space(self):
    s = " s "
    result = "s"
    assert prob.reverseWords(s) == result