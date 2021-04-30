import pytest

from SinglyLinkedList import SinglyLinkedList

import palindrome_SLL as prob

class TestPalindromeSLL:
  def test_example1(self):
    myList = SinglyLinkedList([1,2,2,1])
    assert prob.isPalindrome(myList.getHeadNode()) == True
  

  def test_example2(self):
    myList = SinglyLinkedList([1,2])
    assert prob.isPalindrome(myList.getHeadNode()) == False