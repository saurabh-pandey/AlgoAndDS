import pytest

import array_and_string.array.find_pivot as prob

class TestFindPivot:
  def test_example1(self):
    nums = [1,7,3,6,5,6]
    assert prob.pivotIndex(nums) == 3
  

  def test_example2(self):
    nums = [1,2,3]
    assert prob.pivotIndex(nums) == -1
  

  def test_example3(self):
    nums = [2,1,-1]
    assert prob.pivotIndex(nums) == 0