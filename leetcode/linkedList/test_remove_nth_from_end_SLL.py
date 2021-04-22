import pytest

from SinglyLinkedList import SinglyLinkedList

import remove_nth_from_end_SLL as prob

class TestRemoveNthFromEnd:
  
  def test_example1(self):
    myList = SinglyLinkedList([1,2])

    leftOver = prob.removeNthFromEnd(myList.getHeadNode(), 2)

    output = ""
    currNode = leftOver
    while currNode is not None:
      output += str(currNode._val)
      currNode = currNode._next
      if currNode is not None:
        output += "->"
    print(output)