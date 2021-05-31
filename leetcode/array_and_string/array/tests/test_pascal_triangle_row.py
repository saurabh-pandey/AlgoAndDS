import pytest

import array_and_string.array.pascal_triangle_row as prob

class TestPascalTriangleRow:
  def test_example1(self):
    rowIndex = 3
    result = [1,3,3,1]
    assert prob.getPascalTriangleRow(rowIndex) == result
  

  def test_example2(self):
    rowIndex = 0
    result = [1]
    assert prob.getPascalTriangleRow(rowIndex) == result
  

  def test_example3(self):
    rowIndex = 1
    result = [1, 1]
    assert prob.getPascalTriangleRow(rowIndex) == result
  

  def test_my_example1(self):
    rowIndex = 5
    result = [1, 5, 10, 10, 5, 1]
    assert prob.getPascalTriangleRow(rowIndex) == result