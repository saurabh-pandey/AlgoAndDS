import pytest

import arrays.find_disappeared_nums_a1 as a1
import arrays.find_disappeared_nums_a2 as a2

solutions = {"attempt1_v1": a1.findDisappearedNumbers_O_n_space,
             "attempt1_v2": a1.findDisappearedNumbers_const_space,}
            #  "attempt2": a2.find_disappeared_numbers}

class TestFindDisappearedNumbers:
  def test_example1(self):
    for attempt, solve in solutions.items():
      nums = [4,3,2,7,8,2,3,1]
      disapperedNums = solve(nums)
      expected = [5,6]
      assert disapperedNums == expected, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      nums = [1,1]
      disapperedNums = solve(nums)
      expected = [2]
      assert disapperedNums == expected, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      nums = []
      disapperedNums = solve(nums)
      expected = []
      assert disapperedNums == expected, attempt
  
  def test_single(self):
    for attempt, solve in solutions.items():
      nums = [1]
      disapperedNums = solve(nums)
      expected = [1]
      assert disapperedNums == expected, attempt
