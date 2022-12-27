#URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
# Description
"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that 
has Node.val == val, and return the new head.


Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= k <= 50
"""
def removeElements(head, val):
  if head is None:
    return
  newHead = head
  prevNode = head
  currNode = head
  while currNode is not None:
    if currNode._val == val:
      if currNode is newHead:
        newHead = currNode._next
      else:
        prevNode._next = currNode._next
    else:
      # Only move previous node if current node is not the one to be deleted. Previous node should
      # always point to something that is going to be part of the list
      prevNode = currNode
    currNode = currNode._next
  return newHead