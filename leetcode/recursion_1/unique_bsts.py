#URL: https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/
#Description
"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has 
exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]


Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


nodeCounter = 1

def inorder_traversal(node):
  if node is None:
    return
  global nodeCounter
  inorder_traversal(node.left)
  node.val = nodeCounter
  nodeCounter += 1
  inorder_traversal(node.right)


def cloneTree(root):
  if root is None:
    return None
  newRoot = TreeNode(root.val)
  nodes = [root]
  newNodes = [newRoot]
  while len(nodes) > 0:
    node = nodes.pop(0)
    newNode = newNodes.pop(0)
    if node.left is not None:
      newNode.left = TreeNode(node.left.val)
      nodes.append(node.left)
      newNodes.append(newNode.left)
    if node.right is not None:
      newNode.right = TreeNode(node.right.val)
      nodes.append(node.right)
      newNodes.append(newNode.right)
  return newRoot


def gatherAllOneSidedTrees(n, treesFound, treesMap):
  for root in treesMap[n-1]:
    newRoot1 = TreeNode(0)
    newRoot1.left = cloneTree(root)
    treesFound.append(newRoot1)
    newRoot2 = TreeNode(0)
    newRoot2.right = cloneTree(root)
    treesFound.append(newRoot2)


def gatherAllBothSidedTrees(n, treesFound, treesMap):
  i = 1
  j = n - 2
  while i > 0 and j > 0 and i <= j:
    if i != j:
      subTrees1 = treesMap[i]
      subTrees2 = treesMap[j]
      for root1 in subTrees1:
        for root2 in subTrees2:
          newRoot1 = TreeNode(0)
          newRoot1.left = cloneTree(root1)
          newRoot1.right = cloneTree(root2)
          treesFound.append(newRoot1)
          newRoot2 = TreeNode(0)
          newRoot2.left = cloneTree(root2)
          newRoot2.right = cloneTree(root1)
          treesFound.append(newRoot2)
    else:
      subTrees = treesMap[i]
      for i in range(len(subTrees)):
        for j in range(len(subTrees)):
          newRoot = TreeNode(0)
          newRoot.left = cloneTree(subTrees[i])
          newRoot.right = cloneTree(subTrees[j])
          treesFound.append(newRoot)
    i += 1
    j -= 1


def generateTreesRec(n, treesMap):
  if n not in treesMap:
    if n == 1:
      treesMap[1] = [TreeNode(0)]
    else:
      generateTreesRec(n - 1, treesMap)
      currLevelTrees = []
      gatherAllOneSidedTrees(n, currLevelTrees, treesMap)
      gatherAllBothSidedTrees(n, currLevelTrees, treesMap)
      treesMap[n] = currLevelTrees


def generateTrees(n):
  treesMap = {}
  generateTreesRec(n, treesMap)
  bsts = []
  for tree in treesMap[n]:
    global nodeCounter
    nodeCounter = 1
    inorder_traversal(tree)
    bsts.append(tree)
  return bsts