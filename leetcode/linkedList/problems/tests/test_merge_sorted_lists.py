import pytest

import problems.merge_sorted_lists as prob
import singly_linked_list.operations as sll

class TestMergeSortedList:
  def test_example1(self):
    l1 = [1,2,4]
    l2 = [1,3,4]
    result = [1,1,2,3,4,4]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  
  
  def test_example2(self):
    l1 = []
    l2 = []
    result = []

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  

  def test_example3(self):
    l1 = []
    l2 = [0]
    result = [0]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  

  def test_l1_than_l2(self):
    l1 = [1,2,3]
    l2 = [4,5,6]
    result = [1,2,3,4,5,6]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  

  def test_l2_than_l1(self):
    l1 = [4,5,6]
    l2 = [1,2,3]
    result = [1,2,3,4,5,6]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  
  
  def test_my_example1(self):
    l1 = [1,3,5]
    l2 = [2,4,6,8,10]
    result = [1,2,3,4,5,6,8,10]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  

  def test_my_example2(self):
    l1 = [1,3,5,7,9,11]
    l2 = [2,4,6]
    result = [1,2,3,4,5,6,7,9,11]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
  

  def test_my_example3(self):
    l1 = [1]
    l2 = []
    result = [1]

    myList1 = sll.create(l1)
    myList2 = sll.create(l2)

    mergedList = prob.mergeTwoLists(myList1, myList2)

    assert sll.toList(mergedList) == result
