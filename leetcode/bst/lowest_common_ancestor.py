#URL: https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1012/
#Description
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the 
BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).”


Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to 
the LCA definition.


Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

from leetcode.bst.node import Node


def fill_path(root, target, path):
    currNode = root
    isFound = False
    while currNode:
        path.append(currNode)
        if currNode.val == target.val:
            isFound = True
            break
        if target.val < currNode.val:
            currNode = currNode.left
        else:
            currNode = currNode.right
    return isFound


def lowestCommonAncestor(root, p, q):
    path_to_p = []
    p_is_found = fill_path(root, p, path_to_p)
    if not p_is_found:
        return None
    path_to_q = []
    q_is_found = fill_path(root, q, path_to_q)
    if not q_is_found:
        return None
    lcaNode = None
    for it_p, it_q in zip(path_to_p, path_to_q):
        if it_p.val == it_q.val:
            lcaNode = it_p
        else:
            break
    return lcaNode
