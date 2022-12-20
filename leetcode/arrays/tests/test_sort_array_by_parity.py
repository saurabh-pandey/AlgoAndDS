import pytest

import arrays.sort_array_by_parity_a1 as a1
import arrays.sort_array_by_parity_a2 as a2

solutions = {"attempt1": a1.sortArrayByParity,
             "attempt2": a2.sort_array_by_parity}

class TestSortArrayByParity:
  def test_example1(self):
    for attempt, solve in solutions.items():
      A = [3,1,2,4]
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  
  def test_empty(self):
    for attempt, solve in solutions.items():
      A = []
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  
  def test_all_even(self):
    for attempt, solve in solutions.items():
      A = [2,4,6,8]
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  
  def test_all_odd(self):
    for attempt, solve in solutions.items():
      A = [1,3,5,7,9]
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  
  def test_already_partitioned(self):
    for attempt, solve in solutions.items():
      A = [6,4,2,7,3,5]
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  
  def test_reverse_partitioned(self):
    for attempt, solve in solutions.items():
      A = [3,9,1,6,2,8]
      num_even = self._count_even(A)
      solve(A)
      self._check(A, num_even, attempt)
  

  def _count_even(self, arr):
    return sum(1 - (n % 2) for n in arr)
  
  def _check(self, arr, num_even, attempt):
    allEven = all((x % 2) == 0 for x in arr[:num_even])
    assert allEven, attempt
    allOdd = all((x % 2) == 1 for x in arr[num_even:])
    assert allOdd, attempt
