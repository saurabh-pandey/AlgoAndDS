import pytest

import array_and_string.array.pascal_triangle as prob

class TestPascalTriangle:
  def test_example1(self):
    numRows = 5
    output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    # print(f'Pascal Triangle = {prob.generatePascalTriangle(numRows)}')
    assert prob.generatePascalTriangle(numRows) == output
  

  def test_example2(self):
    numRows = 1
    output = [[1]]
    # print(f'Pascal Triangle = {prob.generatePascalTriangle(numRows)}')
    assert prob.generatePascalTriangle(numRows) == output
  

  def test_empty(self):
    numRows = 0
    output = []
    # print(f'Pascal Triangle = {prob.generatePascalTriangle(numRows)}')
    assert prob.generatePascalTriangle(numRows) == output
  
  def test_my_example1(self):
    numRows = 2
    output = [[1],[1,1]]
    # print(f'Pascal Triangle = {prob.generatePascalTriangle(numRows)}')
    assert prob.generatePascalTriangle(numRows) == output
  

  def test_my_example2(self):
    numRows = 6
    output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
    # print(f'Pascal Triangle = {prob.generatePascalTriangle(numRows)}')
    assert prob.generatePascalTriangle(numRows) == output
