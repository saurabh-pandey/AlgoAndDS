import pytest

import problems.add_two_nums as prob
import singly_linked_list.operations as sll

class TestAddTwoNums:
  def test_example1(self):
    l1 = [2,4,3]
    l2 = [5,6,4]
    result = [7,0,8]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    sumList = prob.addTwoNumbers(myList1, myList2)

    assert sll.toList(sumList) == result
  

  def test_example2(self):
    l1 = [0]
    l2 = [0]
    result = [0]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    sumList = prob.addTwoNumbers(myList1, myList2)

    assert sll.toList(sumList) == result
  

  def test_example3(self):
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    result = [8,9,9,9,0,0,0,1]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    sumList = prob.addTwoNumbers(myList1, myList2)

    assert sll.toList(sumList) == result