#URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
# Description
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement 
both?
"""
def reverseListIterative(head):
  if head is None:
    return None
  
  newHead = head
  oldHead = head
  prevHead = head
  while oldHead._next is not None:
    prevHead = newHead
    newHead = oldHead._next
    oldHead._next = newHead._next
    newHead._next = prevHead
  
  return newHead


def _toList(head):
    output = []
    currNode = head
    while currNode is not None:
      output.append(currNode._val)
      currNode = currNode._next
    return output


def reverseListRecursiveImpl(prevHead, oldHead, newHead):
  if oldHead._next is None:
    return newHead
  
  prevHead = newHead
  newHead = oldHead._next
  oldHead._next = newHead._next
  newHead._next = prevHead
  
  return reverseListRecursiveImpl(prevHead, oldHead, newHead)


def reverseListRecursive(head):
  if head is None:
    return None
  
  return reverseListRecursiveImpl(head, head, head)


def reverseList(head):
  # return reverseListIterative(head)
  return reverseListRecursive(head)