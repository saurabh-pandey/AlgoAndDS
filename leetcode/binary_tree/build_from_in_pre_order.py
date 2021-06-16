#URL: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/
#Description
"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary 
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from binary_tree.node import Node

def buildTreeRecursive(inorder, inStart, inEnd, preorder, preStart, preEnd):
  sz = inEnd - inStart + 1
  assert sz == preEnd - preStart + 1
  if sz <= 0:
    return None
  elif sz == 1:
    return Node(preorder[preStart])
  else:
    rootVal = preorder[preStart]
    rootInorderIndex = -1
    for i in range(inStart, inEnd + 1):
      if inorder[i] == rootVal:
        rootInorderIndex = i
        break
    assert rootInorderIndex >= 0
    leftSz = rootInorderIndex - inStart
    rightSz = inEnd - rootInorderIndex
    leftNode = buildTreeRecursive(inorder, inStart, inStart + leftSz - 1,
                                  preorder, preStart + 1, preStart + leftSz)
    rightNode = buildTreeRecursive(inorder, rootInorderIndex + 1, inEnd,
                                   preorder, preStart + leftSz + 1, preStart + leftSz + rightSz)
    root = Node(rootVal, leftNode, rightNode)
    return root
    


def buildTree(inorder, preorder):
  sz = len(inorder)
  assert sz == len(preorder)
  if sz == 0:
    return None
  
  root = buildTreeRecursive(inorder, 0, sz - 1, preorder, 0, sz - 1)
  # pdb.set_trace()
  return root