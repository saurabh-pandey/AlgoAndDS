import pytest

import even_num_digits as prob

class TestEvenNumDigits:
  def test_case1(self):
    assert prob.findNumbers([12,345,2,6,7896]) == 2
  
  def test_case2(self):
    assert prob.findNumbers([555,901,482,1771]) == 1
  
  def test_empty(self):
    assert prob.findNumbers([]) == 0
  
  def test_case3(self):
    assert prob.findNumbers([1]) == 0
  
  def test_case4(self):
    assert prob.findNumbers([22]) == 1