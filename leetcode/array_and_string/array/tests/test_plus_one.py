import pytest

import array_and_string.array.plus_one as prob

class TestPlusOne:
  def test_example1(self):
    digits = [1,2,3]
    result = [1,2,4]

    assert prob.plusOne(digits) == result
  

  def test_example2(self):
    digits = [4,3,2,1]
    result = [4,3,2,2]

    assert prob.plusOne(digits) == result
  

  def test_example3(self):
    digits = [0]
    result = [1]

    assert prob.plusOne(digits) == result
  

  def test_my_example1(self):
    digits = [9]
    result = [1,0]

    assert prob.plusOne(digits) == result
  

  def test_my_example2(self):
    digits = [9,9,9]
    result = [1,0,0,0]

    assert prob.plusOne(digits) == result
  

  def test_my_example3(self):
    digits = [8,9,9]
    result = [9,0,0]

    assert prob.plusOne(digits) == result
  

  def test_my_example4(self):
    digits = [1,8,9,9]
    result = [1,9,0,0]

    assert prob.plusOne(digits) == result
  

  def test_my_example4(self):
    digits = [1,9,9,2]
    result = [1,9,9,3]

    assert prob.plusOne(digits) == result