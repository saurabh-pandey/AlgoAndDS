import pytest

import arrays.remove_element_a1 as a1
import arrays.remove_element_a2 as a2

solutions = {"attempt1": a1.removeElement, "attempt2": a2.remove_element}

class TestRemoveElement:
  def test_example1(self):
    for attempt, solve in solutions.items():
      nums = [3,2,2,3]
      val = 3
      newLen = solve(nums, val)
      assert newLen == 2, attempt
      expected = [2,2]
      assert expected == nums[:newLen], attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      nums = [0,1,2,2,3,0,4,2]
      val = 2
      newLen = solve(nums, val)
      assert newLen == 5, attempt
      expected = [0,1,4,0,3]
      assert expected == nums[:newLen], attempt
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      nums = []
      val = 2
      newLen = solve(nums, val)
      assert newLen == 0, attempt
      expected = []
      assert expected == nums, attempt
  
  def test_remove_all(self):
    for attempt, solve in solutions.items():
      nums = [1,1,1]
      val = 1
      newLen = solve(nums, val)
      assert newLen == 0, attempt
      expected = []
      assert expected == nums[:newLen], attempt
  
  def test_remove_none(self):
    for attempt, solve in solutions.items():
      nums = [2,2,2]
      val = 1
      newLen = solve(nums, val)
      assert newLen == 3, attempt
      expected = [2,2,2]
      assert expected == nums[:newLen], attempt
  
  def test_another_example(self):
    for attempt, solve in solutions.items():
      nums = [0,4,4,0,4,4,4,0,2]
      val = 4
      newLen = solve(nums, val)
      assert newLen == 4, attempt
      expected = [0,2,0,0]
      assert expected == nums[:newLen], attempt
  