import pytest

import binary_search.find_duplicate as prob

class TestFindDuplicate:
  def test_example1(self):
    nums = [1,3,4,2,2]
    res = 2
    assert prob.findDuplicate(nums) == res
  
  def test_example2(self):
    nums = [3,1,3,4,2]
    res = 3
    assert prob.findDuplicate(nums) == res
  
  def test_example3(self):
    nums = [1,1]
    res = 1
    assert prob.findDuplicate(nums) == res
  
  def test_example4(self):
    nums = [1,1,2]
    res = 1
    assert prob.findDuplicate(nums) == res