import pytest

import random

import binary_search.split_array_sum as prob

class TestSplitArraySum:
  def test_basic_func(self):
    num_trails = 50
    for i in range(num_trails):
      size = random.randint(1, 20)
      nums = [random.randint(0, 50) for i in range(size)]
      m = random.randint(1, 10)
      sums = prob.cummulative_sum(nums)
      nums_sum = sums[-1]
      partitions = [(i + 1) for i in range(m - 1)]
      while prob.isValidPartition(partitions, len(nums)):
        partialSums = prob.findPartialSums(sums, partitions)
        assert nums_sum == sum(partialSums), "Partial sum is wrong"
        prob.nextPartition(partitions, len(nums))
      assert prob.splitArray_iterative(nums, m) == prob.splitArray_recursive(nums, m)
  
  
  def test_example1(self):
    nums = [7,2,5,10,8]
    m = 2
    res = 18
    assert prob.splitArray(nums, m) == res
  
  def test_example2(self):
    nums = [1,2,3,4,5]
    m = 2
    res = 9
    assert prob.splitArray(nums, m) == res
  
  def test_example3(self):
    nums = [1,4,4]
    m = 3
    res = 4
    assert prob.splitArray(nums, m) == res
  
  def test_my_example1(self):
    nums = [1,1,1,1,1,1,100]
    m = 2
    res = 100
    assert prob.splitArray(nums, m) == res
  
  def test_my_example2(self):
    nums = [100,1,1,1,1,1,1]
    m = 2
    res = 100
    assert prob.splitArray(nums, m) == res