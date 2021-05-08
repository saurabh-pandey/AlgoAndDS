from doubly_linked_list.node import Node


def create(in_list):
  """
  Create a Doubly Linked List from input list and return head
  """
  if len(in_list) == 0:
    return None
  
  head = Node(in_list[0])
  currNode = head
  for val in in_list[1:]:
    newNode = Node(val)
    currNode._next = newNode
    newNode._prev = currNode
    currNode = currNode._next
  return head


def addAtHead(head, val):
  newHead = Node(val)
  newHead._next = head
  if head is not None:
    head._prev = newHead
  return newHead


def addAtTail(head, val):
  # If no head then add to tail is same as add to head
  if head is None:
    return addAtHead(head, val)
  else:
    currNode = head
    while currNode is not None:
      if currNode._next is None:
        newTail = Node(val)
        currNode._next = newTail
        newTail._prev = currNode
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
      # New node
      newNode = Node(val)
      # Connect new node's prev and next
      newNode._prev = currNode
      newNode._next = currNode._next
      # Connect the previous and next node
      currNode._next = newNode
      if newNode._next is not None:
        newNode._next._prev = newNode
      break
    depth += 1
    currNode = currNode._next
  return head


def deleteAtIndex(head, index):
  if index == 0 and head is not None:
    shiftedHead = head._next
    head._next = None
    if shiftedHead is not None:
      shiftedHead._prev = None
    return shiftedHead
  
  depth = 0
  currNode = head
  while currNode is not None:
    if depth == index - 1:
      if currNode._next is not None:
        nodeToBeDeleted = currNode._next
        shiftedNode = currNode._next._next
        currNode._next = shiftedNode
        if shiftedNode is not None: 
          shiftedNode._prev = currNode
        nodeToBeDeleted._prev = None
        nodeToBeDeleted._next = None
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


def toString(head, sep = "<=>"):
  """
  Convert a doubly linked list to a string
  """
  output = ""
  currNode = head
  while currNode is not None:
    output += str(currNode._val)
    currNode = currNode._next
    if currNode is not None and currNode._prev is not None:
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