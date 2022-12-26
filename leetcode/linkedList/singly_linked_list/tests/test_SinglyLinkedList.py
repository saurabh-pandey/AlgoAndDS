import pytest

import singly_linked_list.SinglyLinkedList_a1 as a1

solutions = {"attempt1": a1.SinglyLinkedList}

class TestSinglyLinkedList:
    def test_add_simple(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtHead(1)
            myList.addAtTail(3)
            myList.addAtIndex(1,2)
            assert myList.toString() == "1->2->3", attempt
    
    def test_empty(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            assert myList.toString() == "", attempt
    
    def test_add_head_only(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtHead(1)
            assert myList.toString() == "1", attempt
    
    def test_add_tail_only(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtTail(1)
            assert myList.toString() == "1", attempt
    
    def test_add_head_tail(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtHead(1)
            myList.addAtTail(2)
            assert myList.toString() == "1->2", attempt
    
    def test_add_tail_head(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtTail(2)
            myList.addAtHead(1)
            assert myList.toString() == "1->2", attempt
    
    def test_add_index_only(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(0,1)
            myList.addAtIndex(1,2)
            myList.addAtIndex(2,3)
            assert myList.toString() == "1->2->3", attempt
    
    def test_empty_add_index(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(1,1)
            assert myList.toString() == "", attempt
    
    def test_add_index_beyond_size(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(0,1)
            myList.addAtIndex(1,2)
            myList.addAtIndex(2,3)
            
            myList.addAtIndex(6,3)
            assert myList.toString() == "1->2->3", attempt
    
    def test_get(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(0,1)
            myList.addAtIndex(1,2)
            myList.addAtIndex(2,3)

            assert myList.get(0) == 1, attempt
            assert myList.get(1) == 2, attempt
            assert myList.get(2) == 3, attempt
            assert myList.get(3) == -1, attempt
            assert myList.get(4) == -1, attempt
    
    def test_delete(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(0,1)
            myList.addAtIndex(1,2)
            myList.addAtIndex(2,3)

            assert myList.toString() == "1->2->3", attempt
            
            myList.deleteAtIndex(3)
            assert myList.toString() == "1->2->3", attempt

            myList.deleteAtIndex(4)
            assert myList.toString() == "1->2->3", attempt

            myList.deleteAtIndex(0)
            assert myList.toString() == "2->3", attempt

            myList.deleteAtIndex(0)
            assert myList.toString() == "3", attempt

            myList.deleteAtIndex(0)
            assert myList.toString() == "", attempt

            myList.deleteAtIndex(0)
            assert myList.toString() == "", attempt
    
    def test_add_delete(self):
        for attempt, SinglyLinkedList in solutions.items():
            myList = SinglyLinkedList()
            myList.addAtIndex(0,1)
            myList.addAtIndex(1,2)
            myList.addAtIndex(2,3)

            assert myList.toString() == "1->2->3", attempt
            
            myList.deleteAtIndex(1)
            assert myList.toString() == "1->3", attempt

            myList.addAtIndex(1,2)
            assert myList.toString() == "1->2->3", attempt

            myList.deleteAtIndex(2)
            assert myList.toString() == "1->2", attempt
