import pytest

import binary_search.binary_search as prob

class TestBinarySearch:
  def test_example1(self):
    nums = [-1,0,3,5,9,12]
    target = 9
    res = 4
    assert prob.search(nums, target) == res
  
  def test_example2(self):
    nums = [-1,0,3,5,9,12]
    target = 2
    res = -1
    assert prob.search(nums, target) == res
  
  def test_empty(self):
    nums = []
    target = 2
    res = -1
    assert prob.search(nums, target) == res
  
  def test_empty(self):
    nums = []
    target = 2
    res = -1
    assert prob.search(nums, target) == res