#URL: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
#Description
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its 
center).


Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
"""
def isSymmetricIterative(root):
  if root is None:
    return True
  
  leftQueue = [root.left]
  rightQueue = [root.right]
  
  while len(leftQueue) > 0 and len(rightQueue) > 0:
    left = leftQueue.pop(0)
    right = rightQueue.pop(0)
    if left is None and right is None:
      continue
    if left is None and right is not None:
      return False
    if left is not None and right is None:
      return False
    if left.val != right.val:
      return False
    
    # Append left children
    leftQueue.append(left.left)
    leftQueue.append(left.right)
    # Parse right children in reverse i.e. from right to left
    rightQueue.append(right.right)
    rightQueue.append(right.left)
  
  return True


def preorderTraversal(node, preorderList):
  if node is None:
    return
  preorderList.append(node.val)
  preorderTraversal(node.left, preorderList)
  if node.left is None and node.right is not None:
    preorderList.append(None)
  preorderTraversal(node.right, preorderList)
  if node.left is not None and node.right is None:
    preorderList.append(None)


def reversePreorderTraversal(node, revPreorderList):
  if node is None:
    return
  revPreorderList.append(node.val)
  reversePreorderTraversal(node.right, revPreorderList)
  if node.left is not None and node.right is None:
    revPreorderList.append(None)
  reversePreorderTraversal(node.left, revPreorderList)
  if node.left is None and node.right is not None:
    revPreorderList.append(None)

def isSymmetricRecursive(root):
  if root is None:
    return True
  leftSubtreePreorderList = []
  preorderTraversal(root.left, leftSubtreePreorderList)
  rightSubtreePreorderList = []
  reversePreorderTraversal(root.right, rightSubtreePreorderList)

  return leftSubtreePreorderList == rightSubtreePreorderList


def isSymmetric(root, doRecursive=True):
  if doRecursive:
    return isSymmetricRecursive(root)
  else:
    return isSymmetricIterative(root)