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


def generateTrees(n):
  #IDEA
  # In order to solve at n we can break it into 2 cases:
  # 1. Directly use solution from level n-1 and then it can be on the left or right subtree for n
  #   1.1. Thus solution at n-1 becomes twice at level n
  # 2. Now only solve case where the tree is spread across left and right subtree of the root node
  #   2.1. Here again since root node is always involved we have a split
  #   2.2. we use 1, n-2 which means 1 node to the left and n-2 to the right
  #   2.3. Like prev case but invers use n-2, 1 which means 1 node to right and n-2 to the left
  #   2.4. Next is 2, n-3 and n-3, 2
  #   2.5. Similary go till either equal split or split with only 1 difference
  # All above solutions can be stored and reused, thus we need memoization
  pass