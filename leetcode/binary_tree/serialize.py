#URL: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/
#Description
"""
Serialization is the process of converting a data structure or object into a sequence of bits so 
that it can be stored in a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can 
be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do 
not necessarily need to follow this format, so please be creative and come up with different 
approaches yourself.


Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [1]
Output: [1]


Example 4:

Input: root = [1,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
from enum import Enum

class METHOD(Enum):
  LEVEL_ORDER = 0,


def serializeLevelOrder(root):
  if root is None:
    return ""
  
  nodes_queue = [root]
  tree_list = []
  while len(nodes_queue) > 0:
    node = nodes_queue.pop(0)
    if node is None:
      tree_list.append(None)
    else:
      tree_list.append(node.val)
      nodes_queue.append(node.left)
      nodes_queue.append(node.right)
  
  # Trim trailing None
  while tree_list[len(tree_list) - 1] == None:
    tree_list.pop()

  treeStr = ",".join(map(str,tree_list))
  return treeStr



def serialize(root, method=METHOD.LEVEL_ORDER):
  if method is METHOD.LEVEL_ORDER:
    return serializeLevelOrder(root)
  else:
    return "Not implemented"
