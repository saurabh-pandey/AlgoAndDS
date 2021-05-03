from singly_linked_list.node import Node

import singly_linked_list.create_cycle as util
import singly_linked_list.cycle_begin_node as prob

import singly_linked_list.operations as sll

class TestDetectCycleSLL:
  def test_detect_cycle1(self):
    head = sll.create([1,2,3,4])

    assert prob.cycleBeginNode(head) == None
    
    util.createCycle(head, 1)

    assert prob.cycleBeginNode(head)._val == 2
  
  def test_detect_cycle2(self):
    head = sll.create([1,2,3,4])

    assert prob.cycleBeginNode(head) == None
    
    util.createCycle(head, 0)

    assert prob.cycleBeginNode(head)._val == 1
  
  def test_detect_cycle3(self):
    head = sll.create([-1,-7,7,-4,19,6,-9,-5,-2,-5])

    util.createCycle(head, 6)

    assert prob.cycleBeginNode(head)._val == -9