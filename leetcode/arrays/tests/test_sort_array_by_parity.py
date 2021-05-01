import pytest

import arrays.sort_array_by_parity as prob

class TestSortArrayByParity:
  def test_example1(self):
    A = [3,1,2,4]
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd
  
  def test_empty(self):
    A = []
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd
  
  def test_all_even(self):
    A = [2,4,6,8]
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd
  
  def test_all_odd(self):
    A = [1,3,5,7,9]
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd
  
  def test_already_partitioned(self):
    A = [6,4,2,7,3,5]
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd
  
  def test_reverse_partitioned(self):
    A = [3,9,1,6,2,8]
    evenOddPartition = prob.sortArrayByParity(A)
    allEven = all((x % 2) == 0 for x in A[:evenOddPartition])
    assert allEven
    allOdd = all((x % 2) == 1 for x in A[evenOddPartition:])
    assert allOdd