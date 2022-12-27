import singly_linked_list.intersection_a1 as a1

import singly_linked_list.operations_a1 as sll_a1

solutions = {"attempt_1": a1}
slls = {"attempt_1": sll_a1}

class TestLinkedListIntersection:
    def test_example1(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            intersectVal = 8
            listA = [4,1,8,4,5]
            listB = [5,6,1,8,4,5]
            skipA = 2
            skipB = 3
            # Use above input to create intersection
            headA = sll.Node(listA[0])
            headB = sll.Node(listB[0])
            currNodeA = headA
            for i in range(1, skipA):
                currNodeA._next = sll.Node(listA[i])
                currNodeA = currNodeA._next
            
            currNodeB = headB
            for i in range(1, skipB):
                currNodeB._next = sll.Node(listB[i])
                currNodeB = currNodeB._next
            
            for i in range(skipA, len(listA)):
                intersectedNode = sll.Node(listA[i])
                currNodeA._next = intersectedNode
                currNodeB._next = intersectedNode
                currNodeA = currNodeA._next
                currNodeB = currNodeB._next
            
            assert solve.getIntersectionNode(headA, headB)._val == intersectVal


    def test_example2(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            intersectVal = 2
            listA = [1,9,1,2,4]
            listB = [3,2,4]
            skipA = 3
            skipB = 1
            
            # Use above input to create intersection
            headA = sll.Node(listA[0])
            headB = sll.Node(listB[0])
            currNodeA = headA
            for i in range(1, skipA):
                currNodeA._next = sll.Node(listA[i])
                currNodeA = currNodeA._next
            
            currNodeB = headB
            for i in range(1, skipB):
                currNodeB._next = sll.Node(listB[i])
                currNodeB = currNodeB._next
            
            for i in range(skipA, len(listA)):
                intersectedNode = sll.Node(listA[i])
                currNodeA._next = intersectedNode
                currNodeB._next = intersectedNode
                currNodeA = currNodeA._next
                currNodeB = currNodeB._next
            
            assert solve.getIntersectionNode(headA, headB)._val == intersectVal


    def test_example3(self):
        for attempt, solve in solutions.items():
            sll = slls[attempt]
            listA = [2,6,4]
            listB = [1,5]
            skipA = 3
            skipB = 2
            
            # Use above input to create intersection
            headA = sll.Node(listA[0])
            headB = sll.Node(listB[0])
            currNodeA = headA
            for i in range(1, skipA):
                currNodeA._next = sll.Node(listA[i])
                currNodeA = currNodeA._next
            
            currNodeB = headB
            for i in range(1, skipB):
                currNodeB._next = sll.Node(listB[i])
                currNodeB = currNodeB._next
            
            for i in range(skipA, len(listA)):
                intersectedNode = sll.Node(listA[i])
                currNodeA._next = intersectedNode
                currNodeB._next = intersectedNode
                currNodeA = currNodeA._next
                currNodeB = currNodeB._next
            
            assert solve.getIntersectionNode(headA, headB) is None

