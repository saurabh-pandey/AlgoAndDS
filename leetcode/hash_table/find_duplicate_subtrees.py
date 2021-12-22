#URL: https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
#Description
"""
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.


Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]


Example 2:

Input: root = [2,1,1]
Output: [[1]]


Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""

def fill_subtree(node, subtree_dict):
    if node is None:
        return "N"
    key_left = fill_subtree(node.left, subtree_dict)
    key_right = fill_subtree(node.right, subtree_dict)
    key = str(node.val)
    if key_left != "N" or key_right != "N":
        key += "," + key_left + "," + key_right
    if key in subtree_dict:
        subtree_dict[key].append(node)
    else:
        subtree_dict[key] = [node]
    return key

def findDuplicateSubtrees(root):
    if root is None:
        return []
    subtree_dict = {}
    fill_subtree(root, subtree_dict)
    dup_subtrees = []
    for key, nodes in subtree_dict.items():
        if len(nodes) > 1:
            dup_subtrees.append(nodes[0])
    return dup_subtrees
    

    