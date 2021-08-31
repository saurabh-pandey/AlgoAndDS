import pytest

import binary_search.min_rotated_sorted as prob

class TestMinRotatedSorted:
  def test_example1(self):
    nums = [3,4,5,1,2]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_example2(self):
    nums = [4,5,6,7,0,1,2]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_example3(self):
    nums = [11,13,15,17]
    res = 11
    assert prob.findMin(nums) == res
  
  def test_single(self):
    nums = [1]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_rotated_once(self):
    nums = [5,1,2,3,4]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_rotated_last(self):
    nums = [2,3,4,5,1]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_rotated_once_even(self):
    nums = [6,1,2,3,4,5]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_rotated_last_even(self):
    nums = [2,3,4,5,6,1]
    res = 1
    assert prob.findMin(nums) == res