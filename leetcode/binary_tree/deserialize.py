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
import binary_tree.operations as bTree

class METHOD(Enum):
  LEVEL_ORDER = 0,


def deserializeLevelOrder(treeStr):
  if len(treeStr) == 0:
    return None
  
  nodeValStr = treeStr.split(",")
  tree_list = []
  for nodeStr in nodeValStr:
    if nodeStr == "None":
      tree_list.append(None)
    else:
      tree_list.append(int(nodeStr))

  return bTree.create(tree_list)



def deserialize(treeStr, method=METHOD.LEVEL_ORDER):
  if method is METHOD.LEVEL_ORDER:
    return deserializeLevelOrder(treeStr)
  else:
    return "Not implemented"
