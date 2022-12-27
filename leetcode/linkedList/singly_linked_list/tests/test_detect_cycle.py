import singly_linked_list.detect_cycle_a1 as a1

import singly_linked_list.create_cycle_a1 as util_a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
utils = {"attempt_1": util_a1}
slls = {"attempt_1": sll_a1}

class TestDetectCycleSLL:
    def test_detect_cycle1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            util = utils[attempt]
            head = sll.create([1,2,3,4])
            assert solve.detectCycle(head) == False
            util.createCycle(head, 1)
            assert solve.detectCycle(head) == True
    
    
    def test_detect_cycle2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            util = utils[attempt]
            head = sll.create([1,2,3,4])
            assert solve.detectCycle(head) == False
            util.createCycle(head, 0)
            assert solve.detectCycle(head) == True
    
    
    def test_detect_cycle3(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            util = utils[attempt]
            head = sll.create([-1,-7,7,-4,19,6,-9,-5,-2,-5])
            util.createCycle(head, 6)
            assert solve.detectCycle(head) == True
