import pytest

import recursion_2.search_matrix as prob

class TestSearchMatrix:
  def test_example1(self):
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 5
    res = True
    assert prob.searchMatrix(matrix, target) == res
  

  def test_example2(self):
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 20
    res = False
    assert prob.searchMatrix(matrix, target) == res