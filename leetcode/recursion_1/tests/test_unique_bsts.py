import pytest

import recursion_1.unique_bsts as prob

class TestUniqueBsts:
  def test_example1(self):
    n = 3
    res = [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]
    prob.generateTrees(3)
    # assert prob.generateTrees(n) == res