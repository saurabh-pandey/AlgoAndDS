import pytest

import recursion_1.pascal_triangle_rec as prob

class TestPascalTriangleRec:
  def test_example1(self):
    rowIndex = 3
    result = [1,3,3,1]
    assert prob.getRow(rowIndex) == result
  

  def test_example2(self):
    rowIndex = 0
    result = [1]
    assert prob.getRow(rowIndex) == result
  

  def test_example3(self):
    rowIndex = 1
    result = [1, 1]
    assert prob.getRow(rowIndex) == result
  

  def test_my_example1(self):
    rowIndex = 5
    result = [1, 5, 10, 10, 5, 1]
    assert prob.getRow(rowIndex) == result