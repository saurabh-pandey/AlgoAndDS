import pytest

import queue_stack.stack.target_sum as prob

class TestTargetSum:
  def test_example1(self):
    nums = [1,1,1,1,1]
    target = 3
    res = 5
    assert prob.findTargetSumWays(nums, target) == res