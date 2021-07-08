import pytest

import queue_stack.stack.target_sum as prob

class TestTargetSum:
  def test_my_example1(self):
    nums = [1,1]
    target = 0
    res = 2
    assert prob.findTargetSumWays(nums, target) == res
  

  def test_my_example2(self):
    nums = [1,1]
    target = 2
    res = 1
    assert prob.findTargetSumWays(nums, target) == res
  

  def test_my_example3(self):
    nums = [1,1]
    target = -2
    res = 1
    assert prob.findTargetSumWays(nums, target) == res
  
  
  def test_example1(self):
    nums = [1,1,1,1,1]
    target = 3
    res = 5
    assert prob.findTargetSumWays(nums, target) == res
  

  def test_example2(self):
    nums = [1]
    target = 1
    res = 1
    assert prob.findTargetSumWays(nums, target) == res
  
  
  def test_lc_example1(self):
    nums = [44,20,38,6,2,47,18,50,41,38,32,24,38,38,30,5,26,15,37,35]
    target = 44
    print(prob.findTargetSumWays(nums, target))
  