import pytest

import arrays.squares_sorted_array_a1 as a1
import arrays.squares_sorted_array_a2 as a2

solutions = {"attempt1": a1.sort_squares, "attempt2": a2.sort_squares}

class TestSquaresSorted:
  def test_example1(self):
    for attempt, solve in solutions.items():
      nums = [-4,-1,0,3,10]
      result = solve(nums)
      expected = [0,1,9,16,100]
      assert result == expected, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      nums = [-7,-3,2,3,11]
      result = solve(nums)
      expected = [4,9,9,49,121]
      assert result == expected, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      assert solve([]) == [], attempt
  
  def test_no_negative(self):
    for attempt, solve in solutions.items():
      nums = [0,0,2,3,7]
      result = solve(nums)
      expected = [0,0,4,9,49]
      assert result == expected, attempt
  
  def test_no_positive(self):
    for attempt, solve in solutions.items():
      nums = [-7,-4,-1,-1,0]
      result = solve(nums)
      expected = [0,1,1,16,49]
      assert result == expected, attempt
  
  def test_all_zero(self):
    for attempt, solve in solutions.items():
      nums = [0,0,0,0,0]
      result = solve(nums)
      expected = [0,0,0,0,0]
      assert result == expected, attempt
  
