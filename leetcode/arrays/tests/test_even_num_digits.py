import pytest

import arrays.even_num_digits as prob

class TestEvenNumDigits:
  def test_case1(self):
    assert prob.find_numbers([12,345,2,6,7896]) == 2
  
  def test_case2(self):
    assert prob.find_numbers([555,901,482,1771]) == 1
  
  def test_empty(self):
    assert prob.find_numbers([]) == 0
  
  def test_case3(self):
    assert prob.find_numbers([1]) == 0
  
  def test_case4(self):
    assert prob.find_numbers([22]) == 1