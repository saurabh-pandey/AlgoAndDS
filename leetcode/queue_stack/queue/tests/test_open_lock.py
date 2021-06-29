import pytest

import queue_stack.queue.open_lock as prob

class TestOpenLock:
  def test_example1(self):
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    res = 6
    assert prob.openLock(deadends, target) == res
  

  def test_example2(self):
    deadends = ["8888"]
    target = "0009"
    res = 1
    assert prob.openLock(deadends, target) == res
  

  def test_example3(self):
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    res = -1
    assert prob.openLock(deadends, target) == res
  

  def test_example4(self):
    deadends = ["0000"]
    target = "8888"
    res = -1
    assert prob.openLock(deadends, target) == res


  def test_my_example1(self):
    deadends = []
    target = "4"
    res = 4
    assert prob.openLock(deadends, target) == res
  

  def test_my_example2(self):
    deadends = ["3"]
    target = "4"
    res = 6
    assert prob.openLock(deadends, target) == res
  
  
  def test_my_example3(self):
    deadends = ["10"]
    target = "11"
    res = 2
    assert prob.openLock(deadends, target) == res