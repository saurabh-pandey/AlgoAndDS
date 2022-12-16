import pytest

import arrays.find_N_and_double_a1 as a1
import arrays.find_N_and_double_a2 as a2

solutions = {"attempt1": a1.find_N_and_double,
             "attempt2": a2.find_N_and_double}

class TestFindNumAndDoble:
  def test_example1(self):
    for attempt, solve in solutions.items():
      assert solve([10,2,5,3]) == True, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      assert solve([7,1,14,11]) == True, attempt
  
  def test_example3(self):
    for attempt, solve in solutions.items():
      assert solve([3,1,7,11]) == False, attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      assert solve([]) == False, attempt
  
  def test_size_1(self):
    for attempt, solve in solutions.items():
      assert solve([1]) == False, attempt
  
  def test_repetition(self):
    for attempt, solve in solutions.items():
      assert solve([1,1]) == False, attempt
