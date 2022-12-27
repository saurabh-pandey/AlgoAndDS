import singly_linked_list.remove_node_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestRemoveNode:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [1,2,6,3,4,5,6]
            val = 6
            head = sll.create(origList)
            newList = solve.removeElements(head, val)
            assert sll.toList(newList) == [1,2,3,4,5]
    

    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = []
            val = 1
            head = sll.create(origList)
            newList = solve.removeElements(head, val)
            assert sll.toList(newList) == []


    def test_example3(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [7,7,7,7]
            val = 7
            head = sll.create(origList)
            newList = solve.removeElements(head, val)
            assert sll.toList(newList) == []
    

    def test_my_example(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [1,2,3,4]
            val = 5
            head = sll.create(origList)
            newList = solve.removeElements(head, val)
            assert sll.toList(newList) == [1,2,3,4]

    
    def test_lc_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [1,2,2,1]
            val = 2
            head = sll.create(origList)
            newList = solve.removeElements(head, val)
            assert sll.toList(newList) == [1,1]
