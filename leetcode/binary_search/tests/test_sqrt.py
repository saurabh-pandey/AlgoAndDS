import pytest

import math

import binary_search.sqrt as prob

class TestSqrt:
  def test_example1(self):
    x = 4
    res = 2
    assert prob.mySqrt(x) == res
  
  def test_example2(self):
    x = 8
    res = 2
    assert prob.mySqrt(x) == res
  
  def test_some(self):
    nums = [i for i in range(1000)]
    sqrts = [int(math.sqrt(n)) for n in nums]
    for i in range(len(nums)):
      assert prob.mySqrt(nums[i]) == sqrts[i], "Failed for " + str(nums[i])
  
  def test_large(self):
    x = 2000000
    res = 1414
    assert prob.mySqrt(x) == res