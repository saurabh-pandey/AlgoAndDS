import pytest

from SinglyLinkedList import SinglyLinkedList

import linked_list_intersection as prob

class TestLinkedListIntersection:
  def test_example1(self):
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    # Use above input to create intersection
    headA = SinglyLinkedList.Node(4)
    headB = SinglyLinkedList.Node(5)
