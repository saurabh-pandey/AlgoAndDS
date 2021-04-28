import pytest

from SinglyLinkedList import SinglyLinkedList

import odd_even_list as prob

class TestOddEvenList:
  def _toList(self, head):
    output = []
    currNode = head
    while currNode is not None:
      output.append(currNode._val)
      currNode = currNode._next
    return output
  

  def test_example1(self):
    myList = SinglyLinkedList([1,2,3,4,5])
    oddEvenList = prob.oddEvenList(myList.getHeadNode())
    assert self._toList(oddEvenList) == [1,3,5,2,4]
  

  def test_example2(self):
    myList = SinglyLinkedList([2,1,3,5,6,4,7])
    oddEvenList = prob.oddEvenList(myList.getHeadNode())
    assert self._toList(oddEvenList) == [2,3,6,7,1,5,4]