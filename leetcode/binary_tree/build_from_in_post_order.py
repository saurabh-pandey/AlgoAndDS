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

from binary_tree.node import Node

def buildTreeRecursive(inorder, inStart, inEnd, postorder, postStart, postEnd):
  sz = inEnd - inStart + 1
  assert sz == postEnd - postStart + 1
  if sz <= 0:
    return None
  elif sz == 1:
    return Node(postorder[postEnd])
  else:
    rootVal = postorder[postEnd]
    rootInorderIndex = -1
    for i in range(inStart, inEnd + 1):
      if inorder[i] == rootVal:
        rootInorderIndex = i
        break
    assert rootInorderIndex >= 0
    leftSz = rootInorderIndex - inStart
    rightSz = inEnd - rootInorderIndex
    leftNode = buildTreeRecursive(inorder, inStart, inStart + leftSz - 1,
                                  postorder, postStart, postStart + leftSz - 1)
    rightNode = buildTreeRecursive(inorder, rootInorderIndex + 1, inEnd,
                                   postorder, postStart + leftSz, postStart + leftSz + rightSz -1)
    root = Node(rootVal, leftNode, rightNode)
    return root
    


def buildTree(inorder, postorder):
  sz = len(inorder)
  assert sz == len(postorder)
  if sz == 0:
    return None
  
  root = buildTreeRecursive(inorder, 0, sz - 1, postorder, 0, sz - 1)
  return root