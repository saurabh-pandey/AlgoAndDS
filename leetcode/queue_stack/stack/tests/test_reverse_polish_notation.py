import pytest

import queue_stack.stack.reverse_polish_notation as prob

class TestReversePolishNotation:
  def test_example1(self):
    tokens = ["2","1","+","3","*"]
    res = 9
    assert prob.evalRPN(tokens) == res
  

  def test_example2(self):
    tokens = ["4","13","5","/","+"]
    res = 6
    assert prob.evalRPN(tokens) == res
  

  def test_example3(self):
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = 22
    assert prob.evalRPN(tokens) == res
  

  def test_my_example1(self):
    tokens = ["1","2","+"]
    res = 3
    assert prob.evalRPN(tokens) == res
  

  def test_my_example2(self):
    tokens = ["1","2","-"]
    res = -1
    assert prob.evalRPN(tokens) == res
  

  def test_my_example3(self):
    tokens = ["1","2","*"]
    res = 2
    assert prob.evalRPN(tokens) == res
  

  def test_my_example4(self):
    tokens = ["1","2","/"]
    res = 0
    assert prob.evalRPN(tokens) == res
