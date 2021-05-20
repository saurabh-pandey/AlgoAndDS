import pytest

import array_and_string.array.diagonal_traverse as prob

class TestDiagonalTraveral:
  def test_example1(self):
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    # result = [1,2,4,7,5,3,6,8,9]

    print(f'Diagonal list = {prob.findDiagonalOrder(mat)}')

    # assert prob.findDiagonalOrder(mat) == result