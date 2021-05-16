#URL: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
#Description
"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
from singly_linked_list.node import Node as ListNode

def rotateRightOnce(head):
  if head is None or head._next is None:
    return None
  
  prevNode = None
  tailNode = head
  while tailNode._next is not None:
    prevNode = tailNode
    tailNode = tailNode._next
  
  tailNode._next = head
  prevNode._next = None

  return tailNode


def rotateRight(head, k):
  if head is None:
    return None
  
  depth = 0
  currNode = head
  while currNode is not None:
    depth += 1
    currNode = currNode._next

  numRotations = k % depth
  newHead = head
  for i in range(numRotations):
    newHead = rotateRightOnce(newHead)
  
  return newHead

