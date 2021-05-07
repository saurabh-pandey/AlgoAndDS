import pytest

import doubly_linked_list.operations as dll


class TestDoublyLinkedList:
  def test_example1(self):
    inp_list = [1,2,3,4,5]
    head = dll.create(inp_list)
    assert dll.toString(head) == "1<=>2<=>3<=>4<=>5"
    assert dll.toList(head) == inp_list
  

  def test_example2(self):
    head = dll.create([])
    head = dll.addAtHead(head, 1)
    assert dll.toString(head) == "1"

    head = dll.addAtTail(head, 3)
    assert dll.toString(head) == "1<=>3"

    head = dll.addAtIndex(head, 1, 2)
    assert dll.toString(head) == "1<=>2<=>3"


  