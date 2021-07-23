#URL: https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/
#Description
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
def mergeTwoLists(l1, l2):
  head = None
  if l1 is None:
    return l2
  if l2 is None:
    return l1
  if l1._val <= l2._val:
    head = l1
    head._next = mergeTwoLists(l1._next, l2)
  else:
    head = l2
    head._next = mergeTwoLists(l1, l2._next)
  return head
  