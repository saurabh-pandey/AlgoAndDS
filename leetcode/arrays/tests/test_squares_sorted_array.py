import pytest

import arrays.squares_sorted_array as prob

class TestSquaresSorted:
  def test_example1(self):
    nums = [-4,-1,0,3,10]
    result1 = prob.sort_squares_v1(nums)
    result2 = prob.sort_squares_v2(nums)
    expected = [0,1,9,16,100]
    assert result1 == expected
    assert result2 == expected
  
  def test_example2(self):
    nums = [-7,-3,2,3,11]
    result1 = prob.sort_squares_v1(nums)
    result2 = prob.sort_squares_v2(nums)
    expected = [4,9,9,49,121]
    assert result1 == expected
    assert result2 == expected
  
  def test_empty(self):
    assert prob.sort_squares_v1([]) == []
    assert prob.sort_squares_v2([]) == []
  
  def test_no_negative(self):
    nums = [0,0,2,3,7]
    result1 = prob.sort_squares_v1(nums)
    result2 = prob.sort_squares_v2(nums)
    expected = [0,0,4,9,49]
    assert result1 == expected
    assert result2 == expected
  
  def test_no_positive(self):
    nums = [-7,-4,-1,-1,0]
    result1 = prob.sort_squares_v1(nums)
    result2 = prob.sort_squares_v2(nums)
    expected = [0,1,1,16,49]
    assert result1 == expected
    assert result2 == expected
  
  def test_all_zero(self):
    nums = [0,0,0,0,0]
    result1 = prob.sort_squares_v1(nums)
    result2 = prob.sort_squares_v1(nums)
    expected = [0,0,0,0,0]
    assert result1 == expected
    assert result2 == expected
  
