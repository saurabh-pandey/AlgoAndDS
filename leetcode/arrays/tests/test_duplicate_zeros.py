import pytest

import arrays.duplicate_zeros as prob

class TestDuplicateZeros:
  def test_example1(self):
    nums = [1,0,2,3,0,4,5,0]
    prob.duplicate_zeros(nums)
    expected = [1,0,0,2,3,0,0,4]
    assert nums == expected
  
  def test_example2(self):
    nums = [1,2,3]
    prob.duplicate_zeros(nums)
    expected = [1,2,3]
    assert nums == expected
  
  def test_empty(self):
    nums = []
    prob.duplicate_zeros(nums)
    expected = []
    assert nums == expected
  
  def test_all_zeros(self):
    nums = [0,0,0]
    prob.duplicate_zeros(nums)
    expected = [0,0,0]
    assert nums == expected
  
  def test_all_shifted(self):
    nums = [0,0,1,2]
    prob.duplicate_zeros(nums)
    expected = [0,0,0,0]
    assert nums == expected
  
  def test_no_change(self):
    nums = [1,2,3,0]
    prob.duplicate_zeros(nums)
    expected = [1,2,3,0]
    assert nums == expected