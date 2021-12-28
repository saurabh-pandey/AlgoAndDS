#URL: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
#Description
"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [1]
Output: [1]


Example 4:

Input: root = [1,2]
Output: [1,2]


Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from binary_tree.node import Node


def preorderRecursiveImpl(node, preOrderList):
  if node is None:
    return
  
  preOrderList.append(node.val)
  preorderRecursiveImpl(node.left, preOrderList)
  preorderRecursiveImpl(node.right, preOrderList)


def preorderRecursive(root):
  if root is None:
    return []
  
  preOrderList = []
  preorderRecursiveImpl(root, preOrderList)
  return preOrderList


def preorderIterative(root):
  if root is None:
    return []
  
  nodes = [root]
  preOrderList = []
  while len(nodes) > 0:
    node = nodes.pop()
    preOrderList.append(node.val)
    if node.right is not None:
      nodes.append(node.right)
    if node.left is not None:
      nodes.append(node.left)
  return preOrderList


def preorderTraversal(root, doRecursive=True):
  if doRecursive:
    return preorderRecursive(root)
  else:
    return preorderIterative(root)