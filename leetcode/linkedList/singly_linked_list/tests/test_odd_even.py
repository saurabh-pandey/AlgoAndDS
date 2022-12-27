import singly_linked_list.odd_even_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestOddEvenList:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2,3,4,5])
            oddEven = solve.oddEvenList(head)
            assert sll.toList(oddEven) == [1,3,5,2,4]
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([2,1,3,5,6,4,7])
            oddEven = solve.oddEvenList(head)
            assert sll.toList(oddEven) == [2,3,6,7,1,5,4]
