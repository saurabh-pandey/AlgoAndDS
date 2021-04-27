import pytest

from SinglyLinkedList import SinglyLinkedList

import remove_node as prob

class TestRemoveNode:
  def _toList(self, head):
    output = []
    currNode = head
    while currNode is not None:
      output.append(currNode._val)
      currNode = currNode._next
    return output
  

  def test_example1(self):
    origList = [1,2,6,3,4,5,6]
    val = 6
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    assert self._toList(newList) == [1,2,3,4,5]
  

  def test_example2(self):
    origList = []
    val = 1
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    assert self._toList(newList) == []
  

  def test_example3(self):
    origList = [7,7,7,7]
    val = 7
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    assert self._toList(newList) == []
  

  def test_my_example(self):
    origList = [1,2,3,4]
    val = 5
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    assert self._toList(newList) == [1,2,3,4]

  
  def test_lc_example1(self):
    origList = [1,2,2,1]
    val = 2
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    assert self._toList(newList) == [1,1]