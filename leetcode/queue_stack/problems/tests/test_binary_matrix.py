import pytest

import queue_stack.problems.binary_matrix as prob

class TestBinaryMatrix:
  def test_example1(self):
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    res = [[0,0,0],[0,1,0],[0,0,0]]
    assert prob.updateMatrix(mat) == res
  

  def test_example2(self):
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    res = [[0,0,0],[0,1,0],[1,2,1]]
    assert prob.updateMatrix(mat) == res