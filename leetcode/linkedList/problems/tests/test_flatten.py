import pytest

import problems.flatten as prob

import doubly_linked_list.operations as dll

def createMulitlevelList(inpList):
  # Should we use a multi-dim list to constrct this?
  # What about recursion?
  head = None
  currNode = head
  for val in inpList:
    if val is not None:
      newNode = prob.Node(val)
      if head is None:
        head = newNode
        currNode = head
      else:
        currNode.next = newNode
        newNode.prev = currNode
    else:
      # Here create a new list and attach to child
      if currNode is not head:
        currNode = head
      else:
        currNode = currNode._next
  return head

class TestFlatten:
  def test_example1(self):
    input = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    output = [1,2,3,7,8,11,12,9,10,4,5,6]

    head = createMulitlevelList(input)
    
    flattendHead = prob.flatten(head)
    
    assert dll.toList(flattendHead) == output

