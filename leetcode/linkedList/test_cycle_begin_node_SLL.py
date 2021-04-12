from SinglyLinkedList import SinglyLinkedList

import create_cycle_SLL as sll_util
import cycle_begin_node_SLL as prob

class TestDetectCycleSLL:
  def test_detect_cycle1(self):
    myList = SinglyLinkedList([1,2,3,4])

    head = myList.getHeadNode()

    assert prob.cycleBeginNode(head) == None
    
    sll_util.createCycleSLL(myList,1)

    assert prob.cycleBeginNode(head)._val == 2
  
  def test_detect_cycle2(self):
    myList = SinglyLinkedList([1,2,3,4])

    head = myList.getHeadNode()

    assert prob.cycleBeginNode(head) == None
    
    sll_util.createCycleSLL(myList,0)

    assert prob.cycleBeginNode(head)._val == 1
  
  def test_detect_cycle3(self):
    myList = SinglyLinkedList([-1,-7,7,-4,19,6,-9,-5,-2,-5])

    sll_util.createCycleSLL(myList,6)

    head = myList.getHeadNode()

    assert prob.cycleBeginNode(head)._val == -9