import pytest

from singly_linked_list.SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedList:
  
  def test_add_simple(self):
    myList = SinglyLinkedList()
    myList.addAtHead(1)
    myList.addAtTail(3)
    myList.addAtIndex(1,2)
    assert myList.toString() == "1->2->3"
  
  def test_empty(self):
    myList = SinglyLinkedList()
    assert myList.toString() == ""
  
  def test_add_head_only(self):
    myList = SinglyLinkedList()
    myList.addAtHead(1)
    assert myList.toString() == "1"
  
  def test_add_tail_only(self):
    myList = SinglyLinkedList()
    myList.addAtTail(1)
    assert myList.toString() == "1"
  
  def test_add_head_tail(self):
    myList = SinglyLinkedList()
    myList.addAtHead(1)
    myList.addAtTail(2)
    assert myList.toString() == "1->2"
  
  def test_add_tail_head(self):
    myList = SinglyLinkedList()
    myList.addAtTail(2)
    myList.addAtHead(1)
    assert myList.toString() == "1->2"
  
  def test_add_index_only(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)
    assert myList.toString() == "1->2->3"
  
  def test_empty_add_index(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(1,1)
    assert myList.toString() == ""
  
  def test_add_index_beyond_size(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)

    myList.addAtIndex(6,3)
    assert myList.toString() == "1->2->3"
  
  def test_get(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)

    assert myList.get(0) == 1
    assert myList.get(1) == 2
    assert myList.get(2) == 3
    assert myList.get(3) == -1
    assert myList.get(4) == -1
  
  def test_delete(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)

    assert myList.toString() == "1->2->3"
    
    myList.deleteAtIndex(3)
    assert myList.toString() == "1->2->3"

    myList.deleteAtIndex(4)
    assert myList.toString() == "1->2->3"

    myList.deleteAtIndex(0)
    assert myList.toString() == "2->3"

    myList.deleteAtIndex(0)
    assert myList.toString() == "3"

    myList.deleteAtIndex(0)
    assert myList.toString() == ""

    myList.deleteAtIndex(0)
    assert myList.toString() == ""
  
  def test_add_delete(self):
    myList = SinglyLinkedList()
    myList.addAtIndex(0,1)
    myList.addAtIndex(1,2)
    myList.addAtIndex(2,3)

    assert myList.toString() == "1->2->3"
    
    myList.deleteAtIndex(1)
    assert myList.toString() == "1->3"

    myList.addAtIndex(1,2)
    assert myList.toString() == "1->2->3"

    myList.deleteAtIndex(2)
    assert myList.toString() == "1->2"
  
