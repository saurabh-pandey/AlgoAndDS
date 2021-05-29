import pytest

import array_and_string.array.min_subarray_sum as prob

class TestMinSubarraySum:
  def test_example1(self):
    target = 7
    nums = [2,3,1,2,4,3]
    result = 2
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_example2(self):
    target = 4
    nums = [1,4,4]
    result = 1
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_example3(self):
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    result = 0
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_empty(self):
    target = 1
    nums = []
    result = 0
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_size1(self):
    target = 5
    nums = [5]
    result = 1
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_false_size1(self):
    target = 5
    nums = [4]
    result = 0
    assert prob.minSubArrayLen(target, nums) == result
  

  def test_lc_test1(self):
    target = 213
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    result = 8
    assert prob.minSubArrayLen(target, nums) == result
  
