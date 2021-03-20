import pytest

import even_num_digits as prob

class TestEvenNumDigits:
  def test_case1(self):
    assert prob.findNumbers([12,345,2,6,7896]) == 2
  
  def test_case2(self):
    assert prob.findNumbers([555,901,482,1771]) == 1