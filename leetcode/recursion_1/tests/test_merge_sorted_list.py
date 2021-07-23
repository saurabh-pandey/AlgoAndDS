import pytest

import linkedList.singly_linked_list.operations as sll
import recursion_1.merge_sorted_list as prob


class TestMergeTwoSortedLists:
  def test_example1(self):
    l1 = [1,2,4]
    l2 = [1,3,4]
    res = [1,1,2,3,4,4]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_example2(self):
    l1 = []
    l2 = []
    res = []
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_example3(self):
    l1 = []
    l2 = [0]
    res = [0]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_my_example1(self):
    l1 = [1,2]
    l2 = [3,4]
    res = [1,2,3,4]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_my_example2(self):
    l1 = [3,4]
    l2 = [1,2]
    res = [1,2,3,4]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_my_example3(self):
    l1 = [1,2,3]
    l2 = [1,2]
    res = [1,1,2,2,3]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res
  

  def test_my_example4(self):
    l1 = [1,2]
    l2 = [1,2,3]
    res = [1,1,2,2,3]
    myList1 = sll.create(l1)
    myList2 = sll.create(l2)
    mergedList = prob.mergeTwoLists(myList1, myList2)
    assert sll.toList(mergedList) == res