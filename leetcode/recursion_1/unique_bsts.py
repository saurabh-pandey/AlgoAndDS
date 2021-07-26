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
import pdb

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


def toList(root):
  if root is None:
    return []
  
  treeList = [root.val]
  nodes_queue = [root]
  while len(nodes_queue) > 0:
    node = nodes_queue.pop(0)
    lChild = node.left
    rChild = node.right
    if lChild is None and rChild is None:
      continue
    if lChild is not None:
      treeList.append(lChild.val)
      nodes_queue.append(lChild)
    else:
      treeList.append(None)
    if rChild is not None:
      treeList.append(rChild.val)
      nodes_queue.append(rChild)
    else:
      treeList.append(None)
  return treeList


def generateTreesRec(n, treesMap):
  if n not in treesMap:
    if n == 1:
      treesMap[1] = [TreeNode(0)]
    else:
      # pdb.set_trace()
      generateTreesRec(n - 1, treesMap)
      currLevelTrees = []
      for root in treesMap[n-1]:
        newRoot1 = TreeNode(0)
        newRoot1.left = TreeNode(root.val)
        currLevelTrees.append(newRoot1)
        newRoot2 = TreeNode(0)
        newRoot2.right = TreeNode(root.val)
        currLevelTrees.append(newRoot2)
      i = 1
      j = n - 2
      while i > 0 and j > 0 and i <= j:
        if i != j:
          subTrees1 = treesMap[i]
          subTrees2 = treesMap[j]
          for root1 in subTrees1:
            for root2 in subTrees2:
              newRoot1 = TreeNode(0)
              newRoot1.left = TreeNode(root1.val)
              newRoot1.right = TreeNode(root2.val)
              currLevelTrees.append(newRoot1)
              newRoot2 = TreeNode(0)
              newRoot2.left = TreeNode(root2.val)
              newRoot2.right = TreeNode(root1.val)
              currLevelTrees.append(newRoot2)
        else:
          subTrees = treesMap[i]
          for i in range(len(subTrees)):
            for j in range(len(subTrees)):
              newRoot = TreeNode(0)
              newRoot.left = TreeNode(subTrees[i].val)
              newRoot.right = TreeNode(subTrees[j].val)
              currLevelTrees.append(newRoot)
        i += 1
        j -= 1
      treesMap[n] = currLevelTrees



def generateTrees(n):
  treesMap = {}
  generateTreesRec(n, treesMap)
  # for n, trees in treesMap.items():
  #   print(f'For {n} number of trees = {len(trees)}')
  
  bsts = []
  print(f'\nTrees at level {n}:')
  for tree in treesMap[n]:
    global nodeCounter
    nodeCounter = 1
    inorder_traversal(tree)
    bsts.append(toList(tree))
    print(f'  {bsts[-1]}')
  
  return bsts