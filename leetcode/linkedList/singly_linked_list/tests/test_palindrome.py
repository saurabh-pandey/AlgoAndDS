import pytest

import singly_linked_list.operations as sll

import singly_linked_list.palindrome as prob

class TestPalindromeSLL:
  def test_example1(self):
    head = sll.create([1,2,2,1])
    assert prob.isPalindrome(head) == True
  

  def test_example2(self):
    head = sll.create([1,2])
    assert prob.isPalindrome(head) == False