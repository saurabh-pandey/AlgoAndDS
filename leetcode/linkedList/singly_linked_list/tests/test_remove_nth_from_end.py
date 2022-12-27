import singly_linked_list.remove_nth_from_end_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestRemoveNthFromEnd:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2,3,4,5])
            leftOver = solve.removeNthFromEnd(head, 2)
            assert sll.toList(leftOver) == [1,2,3,5]
    
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1])
            leftOver = solve.removeNthFromEnd(head, 1)
            assert sll.toList(leftOver) == []
    
    
    def test_example3(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2])
            leftOver = solve.removeNthFromEnd(head, 1)
            assert sll.toList(leftOver) == [1]
    

    def test_my_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2])
            leftOver = solve.removeNthFromEnd(head, 2)
            assert sll.toList(leftOver) == [2]
