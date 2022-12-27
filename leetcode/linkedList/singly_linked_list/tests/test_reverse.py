import singly_linked_list.reverse_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestReverseSLL:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [1,2,3,4,5]
            head = sll.create(origList)
            reversedList = solve.reverseList(head)
            origList.reverse()
            assert sll.toList(reversedList) == origList
    

    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = [1,2]
            head = sll.create(origList)
            reversedList = solve.reverseList(head)
            origList.reverse()
            assert sll.toList(reversedList) == origList
    

    def test_example3(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            origList = []
            head = sll.create(origList)
            reversedList = solve.reverseList(head)
            origList.reverse()
            assert sll.toList(reversedList) == origList
