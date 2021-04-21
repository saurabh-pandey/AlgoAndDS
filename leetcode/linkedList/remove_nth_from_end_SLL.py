#URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
# Description
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?


Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:

Input: head = [1], n = 1
Output: []


Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
def removeNthFromEnd(head, n):
  firstNode = head
  depth = 0
  secondNode = head
  while firstNode is not None:
    depth += 1
    firstNode = firstNode._next
    if depth > n:
      secondNode = secondNode._next
  
  # Here second node should point to the element to be deleted
  print(f'\t### {n}th node from end = {secondNode._val}')