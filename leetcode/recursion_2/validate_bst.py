#URL: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2874/
#Description
"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

Input: root = [2,1,3]
Output: true


Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
falseValue = (False, None, None)

def isValidBSTRec(root):
  if root.left is not None:
    if root.val <= root.left.val:
      return falseValue
  if root.right is not None:
    if root.val >= root.right.val:
      return falseValue
  
  leftMin = None
  leftMax = None
  if root.left is not None:
    leftSubTr = isValidBSTRec(root.left)
    if leftSubTr[0] == False:
      return falseValue
    leftMin = leftSubTr[1]
    leftMax = leftSubTr[2]
  
  rightMin = None
  rightMax = None
  if root.right is not None:
    rightSubTr = isValidBSTRec(root.right)
    if rightSubTr[0] == False:
      return falseValue
    rightMin = rightSubTr[1]
    rightMax = rightSubTr[2]
  
  if leftMax is not None:
    if root.val <= leftMax:
      return falseValue
  if rightMin is not None:
    if root.val >= rightMin:
      return falseValue
  newMin = leftMin if leftMin is not None else root.val
  newMax = rightMax if rightMax is not None else root.val
  return (True, newMin, newMax)


def isValidBST(root):
  if root is None:
    return False
  isValid, _, _ = isValidBSTRec(root)
  return isValid