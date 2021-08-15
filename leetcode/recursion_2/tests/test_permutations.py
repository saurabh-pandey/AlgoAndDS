import pytest

import recursion_2.permutations as prob

class TestPermutations:
  def checkResult(self, res, out):
    res_set = set([tuple(r) for r in res])
    out_set = set([tuple(o) for o in out])
    assert res_set == out_set
  
  
  def test_example1(self):
    nums = [1,2,3]
    res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    self.checkResult(res, prob.permute(nums))
  

  def test_example2(self):
    nums = [0,1]
    res = [[0,1],[1,0]]
    self.checkResult(res, prob.permute(nums))
  

  def test_example3(self):
    nums = [1]
    res = [[1]]
    self.checkResult(res, prob.permute(nums))