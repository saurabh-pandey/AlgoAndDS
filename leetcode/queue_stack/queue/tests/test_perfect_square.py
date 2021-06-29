import pytest

import queue_stack.queue.perfect_square as prob

class TestPerfectSquare:
  def test_my_example1(self):
    n = 13
    res = [9,4]
    assert prob.numSquares(n) == res
  

  def test_my_example1(self):
    n = 11
    res = [9,1,1]
    assert prob.numSquares(n) == res
  
  # def test_example1(self):
  #   n = 12
  #   res = 3
  #   assert prob.numSquares(n) == res