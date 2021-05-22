import pytest

import array_and_string.array.spiral_traverse as prob

class TestSpiralTraveral:
  def test_example1(self):
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [1,2,3,6,9,8,7,4,5]
    # print(f'Spiral List = {prob.findSpiralOrder(matrix)}')
    # assert prob.findSpiralOrder(matrix) == output
    assert prob.findSpiralOrder(matrix, True) == output
    assert prob.findSpiralOrder(matrix, False) == output
  

  def test_example2(self):
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    output = [1,2,3,4,8,12,11,10,9,5,6,7]
    # print(f'Spiral List = {prob.findSpiralOrder(matrix)}')
    assert prob.findSpiralOrder(matrix, True) == output
    assert prob.findSpiralOrder(matrix, False) == output
  

  def test_empty(self):
    matrix = []
    output = []
    # print(f'Spiral List = {prob.findSpiralOrder(matrix)}')
    assert prob.findSpiralOrder(matrix, True) == output
    assert prob.findSpiralOrder(matrix, False) == output
  

  def test_my_example1(self):
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    output = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    # print(f'Spiral List = {prob.findSpiralOrder(matrix, False)}')
    assert prob.findSpiralOrder(matrix, True) == output
    assert prob.findSpiralOrder(matrix, False) == output