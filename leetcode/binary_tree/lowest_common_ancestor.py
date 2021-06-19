#URL: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
#Description
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).”


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to 
the LCA definition.


Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
def findPathRec(node, elem, path):
  path.append(node)
  if node.val == elem.val:
    return True
  if node.left is not None:
    if findPathRec(node.left, elem, path):
      return True
  if node.right is not None:
    if findPathRec(node.right, elem, path):
      return True
  path.pop()
  return False

def findPath(root, elem):
  if root is None or elem is None:
    return []
  
  path = []
  findPathRec(root, elem, path)
  return path

def lowestCommonAncestor(root, p, q):
  if root is None or p is None or q is None:
    return None
  
  pathP = findPath(root, p)
  pathQ = findPath(root, q)

  minLen = min(len(pathP), len(pathQ))
  lowestCommonAncestorIndex = 0
  for i in range(minLen):
    if pathP[i].val != pathQ[i].val:
      break
    lowestCommonAncestorIndex = i
  return pathP[lowestCommonAncestorIndex]

