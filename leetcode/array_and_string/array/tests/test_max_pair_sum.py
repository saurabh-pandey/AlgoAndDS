import pytest

import array_and_string.array.max_pair_sum as prob

class TestMaxPairSum:
  def test_example1(self):
    nums = [1,4,3,2]
    maxSum = 4
    assert prob.maxPairSum(nums) == maxSum
  

  def test_example2(self):
    nums = [6,2,6,5,1,2]
    maxSum = 9
    assert prob.maxPairSum(nums) == maxSum
  

  def test_empty(self):
    nums = []
    maxSum = 0
    assert prob.maxPairSum(nums) == maxSum
  

  def test_size_2(self):
    nums = [1,1]
    maxSum = 1
    assert prob.maxPairSum(nums) == maxSum
  

  def test_all_same(self):
    nums = [2,2,2,2,2,2]
    maxSum = 6
    assert prob.maxPairSum(nums) == maxSum
  

  def test_sign_mixed(self):
    nums = [-4,-3,-2,-1,0,1,2,3,4,5]
    maxSum = 0
    assert prob.maxPairSum(nums) == maxSum