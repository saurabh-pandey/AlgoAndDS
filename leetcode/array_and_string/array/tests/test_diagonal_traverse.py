import pytest

import array_and_string.array.diagonal_traverse as prob

class TestDiagonalTraveral:
  def test_example1(self):
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    result = [1,2,4,7,5,3,6,8,9]

    assert prob.findDiagonalOrder(mat) == result
  

  def test_example2(self):
    mat = [[1,2],[3,4]]
    result = [1,2,3,4]

    assert prob.findDiagonalOrder(mat) == result
  

  def test_empty(self):
    mat = []
    result = []

    assert prob.findDiagonalOrder(mat) == result
  
  
  def test_size_1(self):
    mat = [[1]]
    result = [1]

    assert prob.findDiagonalOrder(mat) == result

  
  def test_size_4(self):
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    result = [1,2,5,9,6,3,4,7,10,13,14,11,8,12,15,16]

    assert prob.findDiagonalOrder(mat) == result