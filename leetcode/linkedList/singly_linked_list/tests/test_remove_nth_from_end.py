import pytest

import singly_linked_list.operations as sll

import singly_linked_list.remove_nth_from_end as prob

class TestRemoveNthFromEnd:
  
  def test_example1(self):
    head = sll.create([1,2,3,4,5])
    leftOver = prob.removeNthFromEnd(head, 2)
    assert sll.toList(leftOver) == [1,2,3,5]
  
  
  def test_example2(self):
    head = sll.create([1])
    leftOver = prob.removeNthFromEnd(head, 1)
    assert sll.toList(leftOver) == []
  
  
  def test_example3(self):
    head = sll.create([1,2])
    leftOver = prob.removeNthFromEnd(head, 1)
    assert sll.toList(leftOver) == [1]
  

  def test_my_example1(self):
    head = sll.create([1,2])
    leftOver = prob.removeNthFromEnd(head, 2)
    assert sll.toList(leftOver) == [2]