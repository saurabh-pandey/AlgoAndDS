import pytest

import binary_search.min_rotated_duplicate as prob

class TestMinRotatedDuplicate:
  def test_example1(self):
    nums = [1,3,5]
    res = 1
    assert prob.findMin(nums) == res
  
  def test_example2(self):
    nums = [2,2,2,0,1]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_all_same(self):
    nums = [0,0,0,0,0]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_one_diff(self):
    nums = [0,1,1,1,1]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_one_diff_rot(self):
    nums = [1,1,1,0,1,1,1,1]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_multiple_dup(self):
    nums = [3,3,0,0,0,1,1,1,2,2,2,3]
    res = 0
    assert prob.findMin(nums) == res
  
  def test_multiple_dup_min_rot(self):
    nums = [0,0,1,1,1,2,2,2,3,3,3,0]
    res = 0
    assert prob.findMin(nums) == res