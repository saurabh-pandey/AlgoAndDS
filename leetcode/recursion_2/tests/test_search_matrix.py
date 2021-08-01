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
  

  def test_my_example1(self):
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 40
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_row_example1(self):
    matrix = [[1,2,3,5,7,11,13,17]]
    target = 2
    res = True
    assert prob.searchMatrix(matrix, target) == res
  

  def test_row_example2(self):
    matrix = [[1,2,3,5,7,11,13,17]]
    target = 16
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_row_example3(self):
    matrix = [[1,2,3,5,7,11,13,17]]
    target = 0
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_row_example4(self):
    matrix = [[1,2,3,5,7,11,13,17]]
    target = 19
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_col_example1(self):
    matrix = [[1],[2],[3],[5],[7],[11],[13],[17]]
    target = 2
    res = True
    assert prob.searchMatrix(matrix, target) == res
  

  def test_col_example2(self):
    matrix = [[1],[2],[3],[5],[7],[11],[13],[17]]
    target = 16
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_col_example3(self):
    matrix = [[1],[2],[3],[5],[7],[11],[13],[17]]
    target = 0
    res = False
    assert prob.searchMatrix(matrix, target) == res
  

  def test_col_example4(self):
    matrix = [[1],[2],[3],[5],[7],[11],[13],[17]]
    target = 19
    res = False
    assert prob.searchMatrix(matrix, target) == res