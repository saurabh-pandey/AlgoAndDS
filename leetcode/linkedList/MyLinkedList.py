#URL: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
# Description
"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
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
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class Node:
  def __init__(self, val):
    self._val = val
    self._next = None

class MyLinkedList:
  def __init__(self):
    self._head = None
  
  def get(self, index):
    depth = 0
    currNode = self._head
    while currNode is not None:
      if index == depth:
        return currNode._val
      depth += 1
      currNode = currNode._next
    return -1
  
  def addAtHead(self, val):
    if self._head is None:
      self._head = Node(val)
    else:
      newHead = Node(val)
      newHead._next = self._head
      self._head = newHead
  
  def addAtTail(self, val):
    # If no head then add to tail is same as add to head
    if self._head is None:
      self.addAtHead(val)
    
    currNode = self._head
    while currNode is not None:
      if currNode._next is None:
        currNode._next = Node(val)
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
        newNode = Node(val)
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
  
  def toString(self):
    output = ""
    currNode = self._head
    while currNode is not None:
      output += str(currNode._val)
      currNode = currNode._next
      if currNode is not None:
        output += "->"
    return output

def run():
  myList = MyLinkedList()
  print(myList.toString())
  myList.addAtHead(1)
  print(myList.toString())
  myList.addAtTail(3)
  print(myList.toString())
  myList.addAtIndex(1,2)
  print(myList.toString())
  print(myList.get(1))
  myList.deleteAtIndex(1)
  print(myList.toString())
  print(myList.get(1))

run()