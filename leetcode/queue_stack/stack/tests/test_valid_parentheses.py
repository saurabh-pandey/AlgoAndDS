import pytest

import queue_stack.stack.valid_parentheses as prob

class TestValidParentheses:
  def test_example1(self):
    s = "()"
    res = True
    assert prob.isValid(s) == res
  

  def test_example2(self):
    s = "()[]{}"
    res = True
    assert prob.isValid(s) == res
  

  def test_example3(self):
    s = "(]"
    res = False
    assert prob.isValid(s) == res
  

  def test_example4(self):
    s = "([)]"
    res = False
    assert prob.isValid(s) == res
  

  def test_example5(self):
    s = "{[]}"
    res = True
    assert prob.isValid(s) == res
  

  def test_empty(self):
    s = ""
    res = True
    assert prob.isValid(s) == res
  

  def test_my_example1(self):
    s = "((()))"
    res = True
    assert prob.isValid(s) == res
  

  def test_my_example2(self):
    s = "((())"
    res = False
    assert prob.isValid(s) == res
  

  def test_my_example3(self):
    s = "(()))"
    res = False
    assert prob.isValid(s) == res
  

  def test_my_example4(self):
    s = "{[()]}"
    res = True
    assert prob.isValid(s) == res
  

  def test_my_example5(self):
    s = "{[()]"
    res = False
    assert prob.isValid(s) == res