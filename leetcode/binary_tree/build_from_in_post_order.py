#URL: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
#Description
"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary 
tree and postorder is the postorder traversal of the same tree, construct and return the binary 
tree.


Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
def buildTree(inorder, postorder):
  sz = len(inorder)
  assert sz == len(postorder)
  if sz == 0:
    return None

  # Some observations:
  # Post-order's last node is root
  # Now that last node in in-order list will partition the list into left and right subtree
  # Thus we would know the left and right subtree size
  # Based on the sizes we can lookup the root nodes in the left and right subtree from post-order
  # This can go on till we reach a point where the subarray is <=3
  # Now if we have post and in order lists <=3 size we can create the correct Node, Left and Right
  pass