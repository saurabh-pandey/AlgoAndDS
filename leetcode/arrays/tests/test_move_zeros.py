import pytest

import arrays.move_zeros_a1 as a1
import arrays.move_zeros_a2 as a2

solutions = {"attempt1": a1.moveZeroes,
             "attempt2_v1": a2.move_zeros_v1,
             "attempt2_v2": a2.move_zeros_v2}

class TestMoveZeros:
  def test_example1(self):
    for attempt, solve in solutions.items():
      nums = [0,1,0,3,12]
      solve(nums)
      expected = [1,3,12,0,0]
      assert nums == expected, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      nums = [0]
      solve(nums)
      expected = [0]
      assert nums == expected, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      nums = []
      solve(nums)
      expected = []
      assert nums == expected, attempt
  
  def test_all_zeroes(self):
    for attempt, solve in solutions.items():
      nums = [0,0,0,0]
      solve(nums)
      expected = [0,0,0,0]
      assert nums == expected, attempt
  
  def test_last_non_zero(self):
    for attempt, solve in solutions.items():
      nums = [0,0,0,1]
      solve(nums)
      expected = [1,0,0,0]
      assert nums == expected, attempt
