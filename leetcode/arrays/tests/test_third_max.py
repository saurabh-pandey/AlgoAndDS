import pytest

import arrays.third_max_a1 as a1
import arrays.third_max_a2 as a2

solutions = {"attempt1": a1.thirdMax,
             "attempt2": a2.third_max}

class TestThirdMax:
  def test_example1(self):
    for attempt, solve in solutions.items():
      assert solve([3,2,1]) == 1, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      assert solve([1,2]) == 2, attempt
  
  def test_example3(self):
    for attempt, solve in solutions.items():
      assert solve([2,2,3,1]) == 1, attempt
  
  def test_min_thirdmax(self):
    for attempt, solve in solutions.items():
      assert solve([1,2,-2147483648]) == -2147483648, attempt
