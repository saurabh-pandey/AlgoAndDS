import pytest

import arrays.height_checker_a1 as a1
import arrays.height_checker_a2 as a2

solutions = {"attempt1": a1.heightChecker,
             "attempt2": a2.height_checker}

class TestHeightChecker:
  def test_example1(self):
    for attempt, solve in solutions.items():
      heights = [1,1,4,2,1,3]
      numSelected = solve(heights)
      assert numSelected == 3, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      heights = [5,1,2,3,4]
      numSelected = solve(heights)
      assert numSelected == 5, attempt
  
  def test_example3(self):
    for attempt, solve in solutions.items():
      heights = [1,2,3,4,5]
      numSelected = solve(heights)
      assert numSelected == 0, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      heights = []
      numSelected = solve(heights)
      assert numSelected == 0, attempt
  
  def test_reverse(self):
    for attempt, solve in solutions.items():
      heights = [5,4,3,2,1]
      numSelected = solve(heights)
      assert numSelected == 4, attempt
