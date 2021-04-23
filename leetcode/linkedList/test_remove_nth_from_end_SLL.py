import pytest

from SinglyLinkedList import SinglyLinkedList

import remove_nth_from_end_SLL as prob

class TestRemoveNthFromEnd:

  def _toList(self, head):
    output = []
    currNode = head
    while currNode is not None:
      output.append(currNode._val)
      currNode = currNode._next
    return output
  
  
  def test_example1(self):
    myList = SinglyLinkedList([1,2,3,4,5])
    leftOver = prob.removeNthFromEnd(myList.getHeadNode(), 2)
    assert self._toList(leftOver) == [1,2,3,5]
  
  
  def test_example2(self):
    myList = SinglyLinkedList([1])
    leftOver = prob.removeNthFromEnd(myList.getHeadNode(), 1)
    assert self._toList(leftOver) == []
  
  
  def test_example3(self):
    myList = SinglyLinkedList([1,2])
    leftOver = prob.removeNthFromEnd(myList.getHeadNode(), 1)
    assert self._toList(leftOver) == [1]
  

  def test_my_example1(self):
    myList = SinglyLinkedList([1,2])
    leftOver = prob.removeNthFromEnd(myList.getHeadNode(), 2)
    assert self._toList(leftOver) == [2]