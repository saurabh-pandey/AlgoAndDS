import pytest

import arrays.third_max as prob

class TestThirdMax:
  def test_example1(self):
    assert prob.thirdMax([3,2,1]) == 1
  
  def test_example2(self):
    assert prob.thirdMax([1,2]) == 2
  
  def test_example3(self):
    assert prob.thirdMax([2,2,3,1]) == 1
  
  def test_min_thirdmax(self):
    assert prob.thirdMax([1,2,-2147483648]) == -2147483648