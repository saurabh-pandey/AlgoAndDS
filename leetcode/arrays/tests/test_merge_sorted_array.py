import pytest

import arrays.merge_sorted_array_a1 as a1
import arrays.merge_sorted_array_a2 as a2

solutions = {"attempt1": a1.merge, "attempt2": a2.merge}

class TestMergeSortedArray:
  def test_example1(self):
    for attempt, solve in solutions.items():
      nums1 = [1,2,3,0,0,0]
      m = 3
      nums2 = [2,5,6]
      n = 3
      solve(nums1, m, nums2, n)
      expected = [1,2,2,3,5,6]
      assert nums1 == expected, attempt
  
  def test_example2(self):
    for attempt, solve in solutions.items():
      nums1 = [1]
      m = 1
      nums2 = []
      n = 0
      solve(nums1, m, nums2, n)
      expected = [1]
      assert nums1 == expected, attempt
  
  def test_both_empty(self):
    for attempt, solve in solutions.items():
      nums1 = []
      m = 0
      nums2 = []
      n = 0
      solve(nums1, m, nums2, n)
      expected = []
      assert nums1 == expected, attempt
  
  def test_first_empty(self):
    for attempt, solve in solutions.items():
      nums1 = [0]
      m = 0
      nums2 = [1]
      n = 1
      solve(nums1, m, nums2, n)
      expected = [1]
      assert nums1 == expected, attempt
  
  def test_second_smaller(self):
    for attempt, solve in solutions.items():
      nums1 = [7,8,9,0,0,0,0]
      m = 3
      nums2 = [1,2,3,4]
      n = 4
      solve(nums1, m, nums2, n)
      expected = [1,2,3,4,7,8,9]
      assert nums1 == expected, attempt
  
  def test_first_smaller(self):
    for attempt, solve in solutions.items():
      nums1 = [1,2,4,0,0,0,0]
      m = 3
      nums2 = [6,7,8,9]
      n = 4
      solve(nums1, m, nums2, n)
      expected = [1,2,4,6,7,8,9]
      assert nums1 == expected, attempt
  
  def test_alternate(self):
    for attempt, solve in solutions.items():
      nums1 = [1,3,5,0,0,0]
      m = 3
      nums2 = [2,4,6]
      n = 3
      solve(nums1, m, nums2, n)
      expected = [1,2,3,4,5,6]
      assert nums1 == expected, attempt
