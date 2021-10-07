#URL: https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/915/
#Description
"""
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children 
is separated by the null value (See examples).


Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]


Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,
14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""
def levelOrder(root):
  if root is None:
    return []
  level_order_list = []
  nodes = [root]
  while len(nodes) > 0:
    curr_layer = nodes[:]
    nodes = []
    curr_layer_list = []
    for n in curr_layer:
      if n is not None:
        curr_layer_list.append(n.val)
        nodes.extend(n.children)
    level_order_list.append(curr_layer_list)
  return level_order_list
