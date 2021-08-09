#URL: https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2894/
#Description
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the 
same value.


Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
def isSameTreeIterative(p, q):
  pStack = [p]
  qStack = [q]
  while len(pStack) > 0 and len(qStack) > 0:
    currP = pStack.pop()
    currQ = qStack.pop()
    if currP is None and currQ is not None:
      return False
    elif currP is not None and currQ is None:
      return False
    elif currP is not None and currQ is not None:
      if currP.val != currQ.val:
        return False
      pStack.append(currP.right)
      pStack.append(currP.left)
      qStack.append(currQ.right)
      qStack.append(currQ.left)
  return True



def isSameTreeRecursive(p, q):
  if p is None and q is None:
    return True
  elif p is None and q is not None:
    return False
  elif p is not None and q is None:
    return False
  else:
    if p.val != q.val:
      return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTree(p, q, doRecursive = True):
  if doRecursive:
    return isSameTreeRecursive(p, q)
  else:
    return isSameTreeIterative(p, q)