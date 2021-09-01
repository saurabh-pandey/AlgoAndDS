import pytest

import binary_search.search_range as prob

class TestSearchRange:
  def test_example1(self):
    nums = [5,7,7,8,8,10]
    target = 8
    res = [3,4]
    assert prob.searchRange(nums, target) == res
  
  def test_example2(self):
    nums = [5,7,7,8,8,10]
    target = 6
    res = [-1,-1]
    assert prob.searchRange(nums, target) == res
  
  def test_example3(self):
    nums = []
    target = 0
    res = [-1,-1]
    assert prob.searchRange(nums, target) == res
  
  def test_all_same(self):
    nums = [1,1,1,1,1]
    target = 1
    res = [0,4]
    assert prob.searchRange(nums, target) == res
  
  def test_one_match(self):
    nums = [1,2,3,4,5,6]
    target = 2
    res = [1,1]
    assert prob.searchRange(nums, target) == res
  
  def test_last_one_match(self):
    nums = [1,2,3,4,5,6]
    target = 6
    res = [5,5]
    assert prob.searchRange(nums, target) == res
  
  def test_last_three_match(self):
    nums = [1,2,3,4,5,7,7,7]
    target = 7
    res = [5,7]
    assert prob.searchRange(nums, target) == res
  
  def test_first_one_match(self):
    nums = [1,2,3,4,5,6]
    target = 1
    res = [0,0]
    assert prob.searchRange(nums, target) == res
  
  def test_first_three_match(self):
    nums = [1,1,1,2,3,4,5]
    target = 1
    res = [0,2]
    assert prob.searchRange(nums, target) == res