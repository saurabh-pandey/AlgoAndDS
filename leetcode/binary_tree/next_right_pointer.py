#URL: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/
#Description
"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has 
two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the 
next pointer should be set to NULL.
Initially, all next pointers are set to NULL. 

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each 
next pointer to point to its next right node, just like in Figure B. The serialized output is in 
level order as connected by the next pointers, with '#' signifying the end of each level. 


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""
class Node:
  def __init__(self, val, left = None, right = None, next = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next


def connect(root):
  if root is None:
    return None
  
  nodes_per_level = [root]
  nNodesPerLevel = len(nodes_per_level)
  while nNodesPerLevel > 0:
    for i in range(nNodesPerLevel - 1):
      nodes_per_level[i].next = nodes_per_level[i + 1]
    nodes_per_level[nNodesPerLevel - 1].next = None
    next_level_nodes = []
    for node in nodes_per_level:
      if node.left is not None:
        next_level_nodes.append(node.left)
      if node.right is not None:
        next_level_nodes.append(node.right)
    nodes_per_level = next_level_nodes[:]
    nNodesPerLevel = len(nodes_per_level)
  return root


