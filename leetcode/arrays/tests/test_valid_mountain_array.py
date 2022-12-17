import pytest

import arrays.valid_mountain_array_a1 as a1
import arrays.valid_mountain_array_a2 as a2

solutions = {"attempt1": a1.validMountainArray,
             "attempt2": a2.valid_mountain_array}

class TestValidMountainArray:
  def test_example1(self):
    for attempt, solve in solutions.items():
      assert solve([2,1]) == False, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      assert solve([3,5,5]) == False, attempt
  
  def test_example3(self):
    for attempt, solve in solutions.items():
      assert solve([0,3,2,1]) == True, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      assert solve([]) == False, attempt
  
  def test_len_1(self):
    for attempt, solve in solutions.items():
      assert solve([2]) == False, attempt
  
  def test_all_equal(self):
    for attempt, solve in solutions.items():
      assert solve([1,1,1,1]) == False, attempt
  
  def test_some_equal(self):
    for attempt, solve in solutions.items():
      assert solve([0,1,2,2]) == False, attempt
  
  def test_oscillation(self):
    for attempt, solve in solutions.items():
      assert solve([1,4,2,7,3]) == False, attempt
  
  def test_ascending_only(self):
    for attempt, solve in solutions.items():
      assert solve([1,2,3,4,5]) == False, attempt
  
  def test_descending_only(self):
    for attempt, solve in solutions.items():
      assert solve([5,4,3,2,1,0]) == False, attempt

  def test_another_valid(self):
    for attempt, solve in solutions.items():
      assert solve([0,1,2,3,4,5,4,3,2,1,0]) == True, attempt
