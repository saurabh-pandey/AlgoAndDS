import pytest

import singly_linked_list.operations as sll

import singly_linked_list.odd_even as prob

class TestOddEvenList:

  def test_example1(self):
    head = sll.create([1,2,3,4,5])
    oddEven = prob.oddEvenList(head)
    assert sll.toList(oddEven) == [1,3,5,2,4]
  

  def test_example2(self):
    head = sll.create([2,1,3,5,6,4,7])
    oddEven = prob.oddEvenList(head)
    assert sll.toList(oddEven) == [2,3,6,7,1,5,4]