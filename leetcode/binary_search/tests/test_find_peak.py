import pytest

import binary_search.find_peak as prob

class TestFindPeak:
  def test_example1(self):
    nums = [1,2,3,1]
    res = 2
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_example2(self):
    nums = [1,2,1,3,5,6,4]
    res = 5
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_empty(self):
    nums = []
    res = -1
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_single(self):
    nums = [1]
    res = 0
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_two_ascending(self):
    nums = [1, 2]
    res = 1
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_two_descending(self):
    nums = [2, 1]
    res = 0
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_many_ascending(self):
    nums = [1,2,3,4,5,6]
    res = 5
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_many_descending(self):
    nums = [5,4,3,2,1]
    res = 0
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_descending_ascending(self):
    nums = [5,4,3,2,1,2,3,4,5]
    res = 0
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res
  
  def test_lc1(self):
    nums = [3,4,3,2,1]
    res = 1
    assert prob.findPeakElement(nums) == res
    assert prob.findPeakElement(nums, True) == res