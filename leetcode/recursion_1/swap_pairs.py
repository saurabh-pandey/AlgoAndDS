#URL: https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
#Description
"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem 
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]


Example 2:

Input: head = []
Output: []


Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def swapPairsRecursive(node):
  if node is None:
    return node
  
  if node.next is None:
    return node
  
  newHead = node.next
  nextNode = node.next.next
  newHead.next = node
  swappedNode = swapPairsRecursive(nextNode)
  node.next = swappedNode
  return newHead


def swapPairs(head):
  if head is None:
    return None
  
  return swapPairsRecursive(head)