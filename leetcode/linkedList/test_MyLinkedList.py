import pytest

from MyLinkedList import MyLinkedList

class TestMyLinkedList:
  def self_method(self):
    self.myList = MyLinkedList()
  
  def test_scenario0(self):
    assert self.myList.toString() == ""
  
  def test_scenario1(self):
    self.myList.addAtHead(1)
    assert self.myList.toString() == "1"