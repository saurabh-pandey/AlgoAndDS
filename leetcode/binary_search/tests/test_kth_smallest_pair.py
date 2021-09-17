import pytest

import binary_search.kth_smallest_pair as prob

class TestKthSmallestPair:
  def test_example1(self):
    nums = [1,3,1]
    k = 1
    res = 0
    assert prob.kthSmallestDistancePair(nums, k) == res
  
  def test_example2(self):
    nums = [1,1,1]
    k = 2
    res = 0
    assert prob.kthSmallestDistancePair(nums, k) == res
  
  def test_example3(self):
    nums = [1,6,1]
    k = 3
    res = 5
    assert prob.kthSmallestDistancePair(nums, k) == res