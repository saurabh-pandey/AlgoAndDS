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
    nums = 1000
    sqrts = [int(math.sqrt(i)) for i in range(nums)]
    for i in range(nums):
      assert prob.mySqrt(i) == sqrts[i], "Failed for " + str(i)
  
  def test_large(self):
    x = 2000000
    res = int(math.sqrt(x))
    assert prob.mySqrt(x) == res