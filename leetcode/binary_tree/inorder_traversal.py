#URL: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
#Description
"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [1]
Output: [1]


Example 4:

Input: root = [1,2]
Output: [2,1]


Example 5:

Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
def inorderRecursiveImpl(node, inorderList):
  if node.left is not None:
    inorderRecursiveImpl(node.left, inorderList)
  inorderList.append(node.val)
  if node.right is not None:
    inorderRecursiveImpl(node.right, inorderList)


def inorderRecursive(root):
  if root is None:
    return []
  
  inorderList = []
  inorderRecursiveImpl(root, inorderList)
  return inorderList


def inorderTraversal(root, doRecursive=True):
  if doRecursive:
    return inorderRecursive(root)
  else:
    return []
