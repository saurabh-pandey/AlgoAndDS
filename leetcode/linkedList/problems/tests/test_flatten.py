import pytest

import problems.flatten as prob

def toList(head):
  """
  Convert a linked list to a list
  """
  output = []
  currNode = head
  while currNode is not None:
    output.append(currNode.val)
    if currNode.child is not None:
      childList = toList(currNode.child)
      output.append(childList)
    currNode = currNode.next
  return output


def createMulitlevelList(inpList):
  head = None
  currNode = head
  foundChildList = False
  for i in range(len(inpList)):
    val = inpList[i]
    if val is not None:
      if foundChildList:
        newHead = createMulitlevelList(inpList[i:])
        currNode.child = newHead
        return head
      else:
        newNode = prob.Node(val)
        if head is None:
          head = newNode
          currNode = head
        else:
          currNode.next = newNode
          newNode.prev = currNode
          currNode = currNode.next
    else:
      if not foundChildList and currNode is not head:
        currNode = head
      else:
        currNode = currNode.next
      foundChildList = True
  return head

class TestFlatten:
  def test_example1(self):
    input = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    output = [1,2,3,7,8,11,12,9,10,4,5,6]

    head = createMulitlevelList(input)
    flattendHead = prob.flatten(head)
    assert toList(flattendHead) == output
  

  def test_example2(self):
    input = [1,2,None,3]
    output = [1,3,2]

    head = createMulitlevelList(input)
    flattendHead = prob.flatten(head)
    assert toList(flattendHead) == output
  

  def test_example3(self):
    input = []
    output = []

    head = createMulitlevelList(input)
    flattendHead = prob.flatten(head)
    assert toList(flattendHead) == output

