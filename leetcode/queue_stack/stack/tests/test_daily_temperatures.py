import pytest

import queue_stack.stack.daily_temperatures as prob

class TestValidParentheses:
  def test_example1(self):
    temperatures = [73,74,75,71,69,72,76,73]
    res = [1,1,4,2,1,1,0,0]
    assert prob.dailyTemperatures(temperatures) == res
  

  def test_example2(self):
    temperatures = [30,40,50,60]
    res = [1,1,1,0]
    assert prob.dailyTemperatures(temperatures) == res
  

  def test_example3(self):
    temperatures = [30,60,90]
    res = [1,1,0]
    assert prob.dailyTemperatures(temperatures) == res
  

  def test_empty(self):
    temperatures = []
    res = []
    assert prob.dailyTemperatures(temperatures) == res