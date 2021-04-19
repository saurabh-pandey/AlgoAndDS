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
    currNodeA = headA
    for i in range(1, skipA):
      currNodeA._next = SinglyLinkedList.Node(listA[i])
      currNodeA = currNodeA._next
    
    currNodeB = headB
    for i in range(1, skipB):
      currNodeB._next = SinglyLinkedList.Node(listB[i])
      currNodeB = currNodeB._next
    
    for i in range(skipA, len(listA)):
      intersectedNode = SinglyLinkedList.Node(listA[i])
      currNodeA._next = intersectedNode
      currNodeB._next = intersectedNode
      currNodeA = currNodeA._next
      currNodeB = currNodeB._next
    
    assert prob.getIntersectionNode(headA, headB)._val == intersectVal
