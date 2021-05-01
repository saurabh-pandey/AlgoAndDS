import pytest

import arrays.squares_sorted_array as prob

class TestSquaresSorted:
  def test_example1(self):
    nums = [-4,-1,0,3,10]
    result = prob.sortedSquares(nums)
    expected = [0,1,9,16,100]
    assert result == expected
  
  def test_example2(self):
    nums = [-7,-3,2,3,11]
    result = prob.sortedSquares(nums)
    expected = [4,9,9,49,121]
    assert result == expected
  
  def test_empty(self):
    assert prob.sortedSquares([]) == []
  
  def test_no_negative(self):
    nums = [0,0,2,3,7]
    result = prob.sortedSquares(nums)
    expected = [0,0,4,9,49]
    assert result == expected
  
  def test_no_positive(self):
    nums = [-7,-4,-1,-1,0]
    result = prob.sortedSquares(nums)
    expected = [0,1,1,16,49]
    assert result == expected
  
  def test_all_zero(self):
    nums = [0,0,0,0,0]
    result = prob.sortedSquares(nums)
    expected = [0,0,0,0,0]
    assert result == expected