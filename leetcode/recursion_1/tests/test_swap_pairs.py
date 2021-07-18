import pytest

import recursion_1.swap_pairs as prob

def toList(head):
  l = []
  currNode = head
  while currNode is not None:
    l.append(currNode.val)
    currNode = currNode.next
  return l


def create(l):
  head = None
  if len(l) == 0:
    return None
  
  head = prob.ListNode(l[0])
  currNode = head
  for v in l[1:]:
    newNode = prob.ListNode(v)
    currNode.next = newNode
    currNode = currNode.next
  return head

class TestSwapPairs:
  def test_example1(self):
    head = [1,2,3,4]
    headNode = create(head)
    swapPrHead = prob.swapPairs(headNode)
    swapList = toList(swapPrHead)
    res = [2,1,4,3]
    assert swapList == res
  

  def test_example2(self):
    head = [1]
    headNode = create(head)
    swapPrHead = prob.swapPairs(headNode)
    swapList = toList(swapPrHead)
    res = [1]
    assert swapList == res
  

  def test_example3(self):
    head = []
    headNode = create(head)
    swapPrHead = prob.swapPairs(headNode)
    swapList = toList(swapPrHead)
    res = []
    assert swapList == res
  

  def test_my_example1(self):
    head = [1,2,3]
    headNode = create(head)
    swapPrHead = prob.swapPairs(headNode)
    swapList = toList(swapPrHead)
    res = [2,1,3]
    assert swapList == res
  

  def test_my_example2(self):
    head = [1,2,3,4,5]
    headNode = create(head)
    swapPrHead = prob.swapPairs(headNode)
    swapList = toList(swapPrHead)
    res = [2,1,4,3,5]
    assert swapList == res