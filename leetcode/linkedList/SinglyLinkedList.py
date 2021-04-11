#URL: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
# Description
"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the SinglyLinkedList class:

SinglyLinkedList() Initializes the SinglyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid,
return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After
the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked
list. If index equals the length of the linked list, the node will be appended to the end of the
linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["SinglyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
SinglyLinkedList SinglyLinkedList = new SinglyLinkedList();
SinglyLinkedList.addAtHead(1);
SinglyLinkedList.addAtTail(3);
SinglyLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
SinglyLinkedList.get(1);              // return 2
SinglyLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
SinglyLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class SinglyLinkedList:
  '''
  A Node of Singly Linked List
  '''
  class Node:
    def __init__(self, val):
      self._val = val
      self._next = None
  
  def __init__(self, vals = []):
    self._head = None
    for i in range(len(vals)):
      self.addAtIndex(i, vals[i])
  
  def get(self, index):
    depth = 0
    currNode = self._head
    while currNode is not None:
      if index == depth:
        return currNode._val
      depth += 1
      currNode = currNode._next
    return -1
  
  def getNode(self, index):
    depth = 0
    currNode = self._head
    while currNode is not None:
      if index == depth:
        return currNode
      depth += 1
      currNode = currNode._next
    return None
  
  def getHeadNode(self):
    return self.getNode(0)

  def getTailNode(self):
    currNode = self._head
    while currNode is not None:
      nextNode = currNode._next
      if nextNode is None:
        return currNode
      currNode = currNode._next
    return None
  
  def addAtHead(self, val):
    if self._head is None:
      self._head = self.Node(val)
    else:
      newHead = self.Node(val)
      newHead._next = self._head
      self._head = newHead
  
  def addAtTail(self, val):
    # If no head then add to tail is same as add to head
    if self._head is None:
      self.addAtHead(val)
    else:
      currNode = self._head
      while currNode is not None:
        if currNode._next is None:
          currNode._next = self.Node(val)
          break
        currNode = currNode._next
  
  def addAtIndex(self, index, val):
    # Adding to index 0 is same as add to head
    if index == 0:
      self.addAtHead(val)
    
    depth = 0
    currNode = self._head
    while currNode is not None:
      if depth == index - 1:
        newNode = self.Node(val)
        shiftedNode = currNode._next
        currNode._next = newNode
        newNode._next = shiftedNode
        break
      depth += 1
      currNode = currNode._next

  def deleteAtIndex(self, index):
    if index == 0 and self._head is not None:
      shiftedHead = self._head._next
      self._head = shiftedHead
      return
    
    depth = 0
    currNode = self._head
    while currNode is not None:
      if depth == index - 1:
        if currNode._next is not None:
          shiftedNode = currNode._next._next
          currNode._next = shiftedNode
          break
      depth += 1
      currNode = currNode._next
  
  def createCycle(self, index0, index1):
    node0 = self.getNode(index0)
    node1 = self.getNode(index1)
    if node0 is not None and node1 is not None:
      print(f'Creating cycle between {node0._val} and {node1._val}')
      node1._next = node0
  
  def detectCycleNode_O_n2(self):
    distance = 0
    traceNode = self._head
    depth = 0
    currNode = self._head
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
        print(f'WARNING: Cycle starting at node = {traceNode._val}')
        return traceNode
      traceNode = self._head
      distance = 0
    return None
  
  def detectCycleNode(self):
    depth = 0
    slowPtr = self._head
    fastPtr = self._head
    foundCycle = False
    while slowPtr is not None and fastPtr is not None:
      slowPtr = slowPtr._next
      depth += 1
      if fastPtr._next is None:
        break
      fastPtr = fastPtr._next._next

      if fastPtr is slowPtr:
        print(f"Found cycle at depth = {depth} and node = {slowPtr._val}")
        foundCycle = True
        break
    if foundCycle:
      node0 = fastPtr
      node1 = fastPtr._next
      slowPtr = self._head
      depth = 0
      while slowPtr is not None:
        if slowPtr is node0:
          print(f'Cycle starting at node = {node0._val}')
          break
          # return node0
        elif slowPtr is node1:
          print(f'Cycle starting at node = {node1._val}')
          break
          # return node1
        slowPtr = slowPtr._next
    return foundCycle
  
  def toString(self):
    output = ""
    currNode = self._head
    while currNode is not None:
      output += str(currNode._val)
      currNode = currNode._next
      if currNode is not None:
        output += "->"
    return output