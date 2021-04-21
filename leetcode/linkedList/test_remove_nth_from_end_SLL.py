import pytest

from SinglyLinkedList import SinglyLinkedList

import remove_nth_from_end_SLL as prob

class TestRemoveNthFromEnd:
  
  def test_example1(self):
    myList = SinglyLinkedList([1,2,3,4,5])

    prob.removeNthFromEnd(myList.getHeadNode(), 2)