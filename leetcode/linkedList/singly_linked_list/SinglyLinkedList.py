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

from node import Node
import operations

class SinglyLinkedList:
  def __init__(self, vals = []):
    self._head = operations.create(vals)
  
  
  def get(self, index):
    node = operations.getNode(self._head, index)
    if node is not None:
      return node._val
    else:
      return -1
  
  
  def getNode(self, index):
    return operations.getNode(self._head, index)
  
  
  def getHeadNode(self):
    return self._head

  
  def getTailNode(self):
    return operations.getTailNode(self._head)
  
  
  def addAtHead(self, val):
    operations.addAtHead(self._head, val)
  
  
  def addAtTail(self, val):
    operations.addAtTail(self._head, val)
  
  
  def addAtIndex(self, index, val):
    operations.addAtIndex(self._head, index, val)

  
  def deleteAtIndex(self, index):
    operations.deleteAtIndex(self._head, index)

  
  def toString(self):
    operations.toString(self._head)
