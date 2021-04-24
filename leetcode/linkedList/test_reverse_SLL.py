import pytest

from SinglyLinkedList import SinglyLinkedList

import reverse_SLL as prob

class TestReverseSLL:
  def _toList(self, head):
    output = []
    currNode = head
    while currNode is not None:
      output.append(currNode._val)
      currNode = currNode._next
    return output
  
  
  def test_example1(self):
    origList = [1,2,3,4,5]
    myList = SinglyLinkedList(origList)
    reversedList = prob.reverseList(myList.getHeadNode())
    origList.reverse()
    assert self._toList(reversedList) == origList
  

  def test_example2(self):
    origList = [1,2]
    myList = SinglyLinkedList(origList)
    reversedList = prob.reverseList(myList.getHeadNode())
    origList.reverse()
    assert self._toList(reversedList) == origList
  

  def test_example3(self):
    origList = []
    myList = SinglyLinkedList(origList)
    reversedList = prob.reverseList(myList.getHeadNode())
    origList.reverse()
    assert self._toList(reversedList) == origList