#URL: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
#Description
"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from 
left to right, level by level).


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


Example 2:

Input: root = [1]
Output: [[1]]


Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
def levelOrder(root):
  if root is None:
    return []
  
  levelorderList = []
  nodesQueue = [root]
  while len(nodesQueue) > 0:
    depth = len(levelorderList)
    levelorderList.append([])
    currLevelNodes = nodesQueue[:]
    nodesQueue.clear()
    for node in currLevelNodes:
      levelorderList[depth].append(node.val)
      if node.left is not None:
        nodesQueue.append(node.left)
      if node.right is not None:
        nodesQueue.append(node.right)
  return levelorderList
