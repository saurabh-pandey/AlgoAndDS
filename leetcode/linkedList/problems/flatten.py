#URL: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
#Description
"""
You are given a doubly linked list which in addition to the next and previous pointers, it could 
have a child pointer, which may or may not point to a separate doubly linked list. These child 
lists may have one or more children of their own, and so on, to produce a multilevel data 
structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given 
the head of the first level of the list.


Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []


How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the 
upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]


Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
"""

class Node:
  def __init__(self, val, prev = None, next = None, child = None):
    self.val = val
    self.prev = prev
    self.next = next
    self.child = child


def findChildBranch(head):
  currNode = head
  while currNode is not None:
    if currNode.child is not None:
      return currNode
    currNode = currNode.next
  return None


def flatten(head):
  if head is None:
    return None
  
  # Seems like recursion might be the trick
  childBranchNode = findChildBranch(head)
  if childBranchNode is not None:
    flatten(childBranchNode.child)
    nextNode = childBranchNode.next
    childBranchNode.next = childBranchNode.child
    childBranchNode.child.prev = childBranchNode

    tailNode = childBranchNode.child
    while tailNode.next is not None:
      tailNode = tailNode.next
    tailNode.next = nextNode
    if nextNode is not None:
      nextNode.prev = tailNode
    return head
  else:
    return head
  

