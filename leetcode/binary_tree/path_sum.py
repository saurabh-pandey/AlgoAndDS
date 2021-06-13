#URL: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
#Description
"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.


Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true


Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false


Example 3:

Input: root = [1,2], targetSum = 0
Output: false


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
def isLeaf(node):
  assert node is not None
  if node.left is None and node.right is None:
    return True
  return False

def hasPathSumRecursive(node, pathSum, targetSum):
  pathSum += node.val
  if isLeaf(node) and pathSum == targetSum:
      return True
  if node.left is not None:
    if hasPathSumRecursive(node.left, pathSum, targetSum):
      return True
  if node.right is not None:
    if hasPathSumRecursive(node.right, pathSum, targetSum):
      return True
  return False


def hasPathSum(root, targetSum):
  if root is None:
    return False
  return hasPathSumRecursive(root, 0, targetSum)