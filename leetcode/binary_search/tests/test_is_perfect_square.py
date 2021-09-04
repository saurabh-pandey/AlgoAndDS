import pytest

import binary_search.is_perfect_square as prob

class TestIsPerfectSquare:
  def test_example1(self):
    num = 16
    res = True
    assert prob.isPerfectSquare(num) == res
  
  def test_example2(self):
    num = 14
    res = False
    assert prob.isPerfectSquare(num) == res
  
  def test_one(self):
    num = 1
    res = True
    assert prob.isPerfectSquare(num) == res
  
  def test_two(self):
    num = 2
    res = False
    assert prob.isPerfectSquare(num) == res
  
  def test_three(self):
    num = 3
    res = False
    assert prob.isPerfectSquare(num) == res
  
  def test_four(self):
    num = 4
    res = True
    assert prob.isPerfectSquare(num) == res
  
  def test_big(self):
    num = 1000000
    res = True
    assert prob.isPerfectSquare(num) == res