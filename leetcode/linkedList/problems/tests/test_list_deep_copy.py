import pytest

import problems.list_deep_copy as prob


def toList(head):
  output = []
  currNode = head
  while currNode is not None:
    nodeList = [currNode.val]
    if currNode.random is not None:
      nodeList.append(currNode.random.val)
    else:
      nodeList.append(None)
    output.append(nodeList)
    currNode = currNode.next
  return output


def createRandomList(input):
  head = None
  currNode = None
  nodes = []
  for nodeList in input:
    newNode = prob.Node(nodeList[0])
    nodes.append(newNode)
    if head is None:
      head = newNode
      currNode = head
    else:
      currNode.next = newNode
      currNode = currNode.next
  
  for i in range(len(input)):
    nodeList = input[i]
    currNode = nodes[i]
    if nodeList[1] is not None:
      randomId = nodeList[1]
      if randomId < len(nodes):
        randomNode = nodes[randomId]
        currNode.random = randomNode
  return head


class TestListDeepCopy:
  def test_example1(self):
    input = [[7,None],[13,0],[11,4],[10,2],[1,0]]

    head = createRandomList(input)
    copiedList = prob.copyRandomList(head)
    assert toList(copiedList) == toList(head)
  

  def test_example2(self):
    input = [[1,1],[2,1]]

    head = createRandomList(input)
    copiedList = prob.copyRandomList(head)
    assert toList(copiedList) == toList(head)
  

  def test_example3(self):
    input = [[3,None],[3,0],[3,None]]

    head = createRandomList(input)
    copiedList = prob.copyRandomList(head)
    assert toList(copiedList) == toList(head)
  

  def test_example4(self):
    input = []

    head = createRandomList(input)
    copiedList = prob.copyRandomList(head)
    assert toList(copiedList) == toList(head)