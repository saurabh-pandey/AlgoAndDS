#URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
# Description
"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by 
the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the 
input.


Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
 

Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
"""
def oddEvenList(head):
  if head is None:
    return None
  
  lastOddNode = head
  while lastOddNode is not None:
    if lastOddNode._next is None:
      break
    elif lastOddNode._next._next is None:
      break
    lastOddNode = lastOddNode._next._next
  
  # depth = 1
  prevNode = head
  evenNode = head._next
  shiftingPoint = lastOddNode
  while evenNode is not None:
    prevNode._next = evenNode._next
    evenNode._next = shiftingPoint._next
    shiftingPoint._next = evenNode
    shiftingPoint = evenNode
    prevNode = prevNode._next
    if prevNode is lastOddNode:
      break
    evenNode = prevNode._next
  
  return head
    


  
  
  