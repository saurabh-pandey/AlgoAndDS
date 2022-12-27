import singly_linked_list.palindrome_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestPalindromeSLL:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2,2,1])
            assert solve.isPalindrome(head) == True
    
    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2])
            assert solve.isPalindrome(head) == False
    
    def test_odd_size_1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            head = sll.create([1,2,3,2,1])
            assert solve.isPalindrome(head) == True
