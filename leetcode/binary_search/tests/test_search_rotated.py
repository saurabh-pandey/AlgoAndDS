import pytest

import binary_search.search_rotated as prob

class TestSearchRotated:
  def test_example1(self):
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = 4
    assert prob.search_rotated(nums, target) == res
  
  def test_example2(self):
    nums = [4,5,6,7,0,1,2]
    target = 3
    res = -1
    assert prob.search_rotated(nums, target) == res
  
  def test_example3(self):
    nums = [1]
    target = 0
    res = -1
    assert prob.search_rotated(nums, target) == res
  
  def test_empty(self):
    nums = []
    target = 0
    res = -1
    assert prob.search_rotated(nums, target) == res
  
  def test_sorted(self):
    nums = [0,1,2,3,4,5]
    target = 3
    res = 3
    assert prob.search_rotated(nums, target) == res