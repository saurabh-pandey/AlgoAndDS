import pytest

import singly_linked_list.operations as sll

import singly_linked_list.remove_node as prob

class TestRemoveNode:

  def test_example1(self):
    origList = [1,2,6,3,4,5,6]
    val = 6
    head = sll.create(origList)
    newList = prob.removeElements(head, val)
    assert sll.toList(newList) == [1,2,3,4,5]
  

  def test_example2(self):
    origList = []
    val = 1
    head = sll.create(origList)
    newList = prob.removeElements(head, val)
    assert sll.toList(newList) == []
  

  def test_example3(self):
    origList = [7,7,7,7]
    val = 7
    head = sll.create(origList)
    newList = prob.removeElements(head, val)
    assert sll.toList(newList) == []
  

  def test_my_example(self):
    origList = [1,2,3,4]
    val = 5
    head = sll.create(origList)
    newList = prob.removeElements(head, val)
    assert sll.toList(newList) == [1,2,3,4]

  
  def test_lc_example1(self):
    origList = [1,2,2,1]
    val = 2
    head = sll.create(origList)
    newList = prob.removeElements(head, val)
    assert sll.toList(newList) == [1,1]