import pytest

import recursion_2.combinations as prob

class TestCombinations:
  def checkResult(self, res, output):
    res_tup = set([tuple(r) for r in res])
    out_tup = set([tuple(r) for r in output])
    assert res_tup == out_tup
  
  
  def test_example1(self):
    n = 4
    k = 2
    res =  [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
    self.checkResult(res, prob.combine(n, k))
  

  def test_example2(self):
    n = 1
    k = 1
    res =  [[1]]
    self.checkResult(res, prob.combine(n, k))
  

  def test_my_example1(self):
    n = 4
    k = 3
    res =  [[1,2,3], [1,2,4], [1,3,4], [2,3,4]]
    self.checkResult(res, prob.combine(n, k))
  

  def test_my_example2(self):
    n = 2
    k = 2
    res =  [[1,2]]
    self.checkResult(res, prob.combine(n, k))
  

  def test_my_example3(self):
    n = 3
    k = 1
    res =  [[1], [2], [3]]
    self.checkResult(res, prob.combine(n, k))