#URL: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
#Description
"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
to the farthest leaf node.
 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3


Example 2:

Input: root = [1,null,2]
Output: 2


Example 3:

Input: root = []
Output: 0


Example 4:

Input: root = [0]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
max_depth = 0

def maxDepthTopDownImpl(node, depth):
  if node.left is None and node.right is None:
    global max_depth
    max_depth = depth if depth > max_depth else max_depth
  if node.left is not None:
    maxDepthTopDownImpl(node.left, depth + 1)
  if node.right is not None:
    maxDepthTopDownImpl(node.right, depth + 1)


def maxDepthTopDown(root):
  if root is None:
    return 0
  
  global max_depth
  max_depth = 0
  maxDepthTopDownImpl(root, 1)
  return max_depth


def maxDepthBottomUp(root):
  if root is None:
    return 0
  
  leftSubtreeDepth = maxDepthBottomUp(root.left)
  rightSubtreeDepth = maxDepthBottomUp(root.right)
  return max(leftSubtreeDepth, rightSubtreeDepth) + 1


def maxDepth(root, doTopDown=True):
  if doTopDown:
    return maxDepthTopDown(root)
  else:
    return maxDepthBottomUp(root)