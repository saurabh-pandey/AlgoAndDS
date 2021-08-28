import pytest

import binary_search.guess_num as prob

class TestGuessNum:
  def test_example1(self):
    n = 10
    picked = prob.PickedNum(n)
    assert prob.guessNumber(n, picked) == picked.pick()
  
  def test_example2(self):
    n = 1
    picked = prob.PickedNum(n)
    assert prob.guessNumber(n, picked) == picked.pick()
  
  def test_example3(self):
    n = 2
    picked = prob.PickedNum(n)
    assert prob.guessNumber(n, picked) == picked.pick()