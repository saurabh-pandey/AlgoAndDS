import pytest

from SinglyLinkedList import SinglyLinkedList

import detect_cycle_SLL as prob

class TestDetectCycleSLL:
  def test_detect_cycle1(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)
    myList.addAtIndex(3,4)

    assert prob.detectCycleNode() == False
    
    myList.createCycle(1,3)

    assert myList.detectCycleNode() == True
  
  def test_detect_cycle2(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)
    myList.addAtIndex(3,4)

    assert myList.detectCycleNode() == False
    
    myList.createCycle(0,3)

    assert myList.detectCycleNode() == True
  
  def test_detect_cycle3(self):
    myList = SinglyLinkedList([-1,-7,7,-4,19,6,-9,-5,-2,-5])
    print(myList.toString())

    myList.createCycle(6,9)

    assert myList.detectCycleNode() == True