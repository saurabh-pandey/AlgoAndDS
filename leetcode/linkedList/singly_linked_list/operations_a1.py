from singly_linked_list.node_a1 import Node


def create(in_list):
  """
  Create a Singly Linked List from input list and return head
  """
  if len(in_list) == 0:
    return None
  
  head = Node(in_list[0])
  currNode = head
  for val in in_list[1:]:
    newNode = Node(val)
    currNode._next = newNode
    currNode = currNode._next
  return head


def addAtHead(head, val):
  newHead = Node(val)
  newHead._next = head
  head = newHead
  return newHead


def addAtTail(head, val):
  # If no head then add to tail is same as add to head
  if head is None:
    return addAtHead(head, val)
  else:
    currNode = head
    while currNode is not None:
      if currNode._next is None:
        currNode._next = Node(val)
        break
      currNode = currNode._next
    return head


def addAtIndex(head, index, val):
  # Adding to index 0 is same as add to head
  if index == 0:
    return addAtHead(head, val)
  
  depth = 0
  currNode = head
  while currNode is not None:
    if depth == index - 1:
      newNode = Node(val)
      shiftedNode = currNode._next
      currNode._next = newNode
      newNode._next = shiftedNode
      break
    depth += 1
    currNode = currNode._next
  return head


def deleteAtIndex(head, index):
  if index == 0 and head is not None:
    shiftedHead = head._next
    head = shiftedHead
    return head
  
  depth = 0
  currNode = head
  while currNode is not None:
    if depth == index - 1:
      if currNode._next is not None:
        shiftedNode = currNode._next._next
        currNode._next = shiftedNode
        break
    depth += 1
    currNode = currNode._next
  return head


def getNode(head, index):
  depth = 0
  currNode = head
  while currNode is not None:
    if index == depth:
      return currNode
    depth += 1
    currNode = currNode._next
  return None


def getTailNode(head):
  currNode = head
  while currNode is not None:
    nextNode = currNode._next
    if nextNode is None:
      return currNode
    currNode = nextNode
  return None


def size(head):
  depth = 0
  currNode = head
  while currNode is not None:
    depth += 1
    currNode = currNode._next
  return depth


def toString(head, sep = "->"):
  """
  Convert a linked list to a string
  """
  output = ""
  currNode = head
  while currNode is not None:
    output += str(currNode._val)
    currNode = currNode._next
    if currNode is not None:
      output += sep
  return output


def toList(head):
  """
  Convert a linked list to a list
  """
  output = []
  currNode = head
  while currNode is not None:
    output.append(currNode._val)
    currNode = currNode._next
  return output