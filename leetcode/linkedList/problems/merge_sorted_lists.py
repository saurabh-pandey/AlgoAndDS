#URL: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
# Description
"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing 
together the nodes of the first two lists.


Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

import singly_linked_list.node.Node as ListNode

def mergeTwoLists(l1, l2):
  firstPtr = l1
  secondPtr = l2
  mergedList = None
  currNode = mergedList
  while firstPtr is not None and secondPtr is not None:
    if firstPtr._val < secondPtr._val:
      newNode = ListNode(firstPtr._val)
      if mergedList is None:
        mergedList = newNode
        currNode = mergedList
      else:
        currNode._next = newNode
        currNode = currNode._next
      firstPtr = firstPtr._next
    else:
      newNode = ListNode(secondPtr._val)
      if mergedList is None:
        mergedList = newNode
        currNode = mergedList
      else:
        currNode._next = newNode
        currNode = currNode._next
      secondPtr = secondPtr._next
  if firstPtr is not None:
    newNode = ListNode(firstPtr._val)
    if mergedList is None:
      mergedList = newNode
      currNode = mergedList
    else:
      currNode._next = newNode
      currNode = currNode._next
    firstPtr = firstPtr._next
  if secondPtr is not None:
    newNode = ListNode(secondPtr._val)
    if mergedList is None:
      mergedList = newNode
      currNode = mergedList
    else:
      currNode._next = newNode
      currNode = currNode._next
    secondPtr = secondPtr._next
