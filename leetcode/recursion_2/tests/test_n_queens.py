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