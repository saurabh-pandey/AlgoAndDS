import pytest

import arrays.move_zeros as prob

class TestMoveZeros:
  def test_example1(self):
    nums = [0,1,0,3,12]
    prob.moveZeroes(nums)
    expected = [1,3,12,0,0]
    assert nums == expected
  
  def test_example2(self):
    nums = [0]
    prob.moveZeroes(nums)
    expected = [0]
    assert nums == expected
  
  def test_empty(self):
    nums = []
    prob.moveZeroes(nums)
    expected = []
    assert nums == expected
  
  def test_all_zeroes(self):
    nums = [0,0,0,0]
    prob.moveZeroes(nums)
    expected = [0,0,0,0]
    assert nums == expected
  
  def test_last_non_zero(self):
    nums = [0,0,0,1]
    prob.moveZeroes(nums)
    expected = [1,0,0,0]
    assert nums == expected