

from SinglyLinkedList import SinglyLinkedList

def detectCycleSLL_O_n2(head):
  distance = 0
  traceNode = head
  depth = 0
  currNode = head
  while currNode is not None:
    depth += 1
    currNode = currNode._next
    while traceNode is not None:
      if traceNode is currNode:
        break
      traceNode = traceNode._next
      distance += 1
    # if currNode is not None:
      # print(f'Distance from head to {currNode._val} is {distance} and depth = {depth}')
    if distance != depth:
      print(f'WARNING: Cycle detected at distance = {distance} and depth = {depth}')
      return True
    traceNode = head
    distance = 0
  return False

def detectCycleSLL_O_n(head):
  depth = 0
  slowPtr = head
  fastPtr = head
  while slowPtr is not None and fastPtr is not None:
    slowPtr = slowPtr._next
    depth += 1
    if fastPtr._next is None:
      break
    fastPtr = fastPtr._next._next

    if fastPtr is slowPtr:
      print(f"Found cycle at depth = {depth} and node = {slowPtr._val}")
      return True
  return False

def detectCycleSLL(head):
  return detectCycleSLL_O_n(head)
  # return detectCycleSLL_O_n2(head)