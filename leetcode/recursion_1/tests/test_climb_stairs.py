import pytest

import recursion_1.climb_stairs as prob

class TestClimbStairs:
  def test_example1(self):
    n = 2
    res = 2
    assert prob.climbStairs(n) == res
  

  def test_example2(self):
    n = 3
    res = 3
    assert prob.climbStairs(n) == res
  

  def test_my_example1(self):
    n = 1
    res = 1
    assert prob.climbStairs(n) == res
  

  def test_my_example2(self):
    n = 4
    res = 5
    assert prob.climbStairs(n) == res
  

  def test_my_example3(self):
    n = 5
    res = 8
    assert prob.climbStairs(n) == res