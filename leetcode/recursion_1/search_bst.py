#URL: https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/
#Description
"""
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that 
node. If such a node does not exist, return null.


Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def searchBST(root, val):
  if root is None:
    return None
  if root.val == val:
    return root
  
  if val < root.val:
    return searchBST(root.left, val)
  else: # val > root.val
    return searchBST(root.right, val)