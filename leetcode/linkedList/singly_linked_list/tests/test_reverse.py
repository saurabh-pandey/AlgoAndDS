import pytest

import singly_linked_list.operations as sll

import singly_linked_list.reverse as prob

class TestReverseSLL:

  def test_example1(self):
    origList = [1,2,3,4,5]
    head = sll.create(origList)
    reversedList = prob.reverseList(head)
    origList.reverse()
    assert sll.toList(reversedList) == origList
  

  def test_example2(self):
    origList = [1,2]
    head = sll.create(origList)
    reversedList = prob.reverseList(head)
    origList.reverse()
    assert sll.toList(reversedList) == origList
  

  def test_example3(self):
    origList = []
    head = sll.create(origList)
    reversedList = prob.reverseList(head)
    origList.reverse()
    assert sll.toList(reversedList) == origList