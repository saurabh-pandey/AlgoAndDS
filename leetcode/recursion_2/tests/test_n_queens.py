import pytest

import recursion_2.n_queens as prob

class TestN_Queens:
  def test_example1(self):
    n = 4
    res = 2
    assert prob.totalNQueens(n) == res
  

  def test_example2(self):
    n = 1
    res = 1
    assert prob.totalNQueens(n) == res
  
  
  def test_my_example1(self):
    n = 2
    res = 0
    assert prob.totalNQueens(n) == res
  

  def test_my_example2(self):
    n = 3
    res = 0
    assert prob.totalNQueens(n) == res
  

  def test_my_example3(self):
    n = 5
    res = 10
    assert prob.totalNQueens(n) == res
  

  def test_my_example4(self):
    n = 6
    res = 4
    assert prob.totalNQueens(n) == res
  

  def test_my_example5(self):
    n = 7
    res = 40
    assert prob.totalNQueens(n) == res
  

  def test_my_example6(self):
    n = 8
    res = 92
    assert prob.totalNQueens(n) == res
  

  def test_my_example7(self):
    n = 9
    res = 352
    assert prob.totalNQueens(n) == res