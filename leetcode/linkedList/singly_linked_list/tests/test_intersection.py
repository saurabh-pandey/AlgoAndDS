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
    headA = SinglyLinkedList.Node(listA[0])
    headB = SinglyLinkedList.Node(listB[0])
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
  
  
  def test_example2(self):
    intersectVal = 2
    listA = [1,9,1,2,4]
    listB = [3,2,4]
    skipA = 3
    skipB = 1
    
    # Use above input to create intersection
    headA = SinglyLinkedList.Node(listA[0])
    headB = SinglyLinkedList.Node(listB[0])
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
  

  def test_example3(self):
    intersectVal = 0
    listA = [2,6,4]
    listB = [1,5]
    skipA = 3
    skipB = 2
    
    # Use above input to create intersection
    headA = SinglyLinkedList.Node(listA[0])
    headB = SinglyLinkedList.Node(listB[0])
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
    
    assert prob.getIntersectionNode(headA, headB) is None

