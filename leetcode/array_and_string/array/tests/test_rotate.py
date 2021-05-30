import pytest

import array_and_string.array.rotate as prob

class TestRotate:
  def test_example1(self):
    nums = [1,2,3,4,5,6,7]
    k = 3
    result = [5,6,7,1,2,3,4]
    prob.rotate(nums, k)
    assert nums == result
  

  def test_example2(self):
    nums = [-1,-100,3,99]
    k = 2
    result = [3,99,-1,-100]
    prob.rotate(nums, k)
    assert nums == result
  

  def test_empty(self):
    nums = []
    k = 2
    result = []
    prob.rotate(nums, k)
    assert nums == result
  

  def test_size_1(self):
    nums = [1]
    k = 2
    result = [1]
    prob.rotate(nums, k)
    assert nums == result
  

  def test_size_2(self):
    nums = [1,2]
    k = 1
    result = [2,1]
    prob.rotate(nums, k)
    assert nums == result