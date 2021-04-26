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
    origList = [1,2,2,1]
    val = 2
    myList = SinglyLinkedList(origList)
    newList = prob.removeElements(myList.getHeadNode(), val)
    print(f'\t### origList = {origList}, newList = {self._toList(newList)}')