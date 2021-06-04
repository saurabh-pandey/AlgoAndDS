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

import pdb

def preorder(node, preOrderList):
  # pdb.set_trace()
  if node is None:
    return
  
  preOrderList.append(node.val)
  preorder(node.left, preOrderList)
  preorder(node.right, preOrderList)

def preorderTraversal(root):
  if root is None:
    return []
  
  preOrderList = []
  preorder(root, preOrderList)
  return preOrderList