#URL: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Description
"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists 
intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:

It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.


Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists 
intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There 
are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists 
intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 
nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?
"""
def nextNode(currNodeA, currNodeB):
  if currNodeA._next is None and currNodeB._next is None:
    # Reached the tail of both lists
    return
  elif currNodeA._next is None and currNodeB._next is not None:
    # Reached the tail of A so continue diving only in B
    nextNode(currNodeA, currNodeB._next)
  elif currNodeA._next is not None and currNodeB._next is None:
    # Reached the tail of B so continue diving only in A
    nextNode(currNodeA._next, currNodeB)
  else:
    # Still not reached the tail of both A and B continue diving
    nextNode(currNodeA._next, currNodeB._next)


def getIntersectionNode(headA, headB):
  """
  IDEA 1: The idea is to reach the tail of both the lists and the climb upwards till reaching a 
  branching point. Probably using recursion.
  IDEA 2: Use stack instead of recursion. Try this one first.
  """
  stackA = []
  nodeA = headA
  while nodeA is not None:
    stackA.append(nodeA)
    nodeA = nodeA._next
  
  stackB = []
  nodeB = headB
  while nodeB is not None:
    stackB.append(nodeB)
    nodeB = nodeB._next
  
  intersectedNode = None
  while len(stackA) > 0 and len(stackB) > 0:
    nodeA = stackA.pop()
    nodeB = stackB.pop()
    if nodeA is nodeB:
      intersectedNode = nodeA
      continue
    else:
      break
  
  return intersectedNode
    