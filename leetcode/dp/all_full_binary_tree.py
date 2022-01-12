#URL: https://leetcode.com/problems/all-possible-full-binary-trees/
#Description
"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each 
tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of 
trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.


Example 1:

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]


Example 2:

Input: n = 3
Output: [[0,0,0]]


Constraints:

1 <= n <= 20
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return not node.left and not node.right 


def fetchAllLeaves(node):
    leaves = []
    if isLeaf(node):
        leaves.append(node)
    else:
        leaves.extend(fetchAllLeaves(node.left))
        leaves.extend(fetchAllLeaves(node.right))
    return leaves



def allPossibleFBT(n):
    # A rolling buffer of two trees
    fullFBTs = [None, None]
    fullFBTs[0] = TreeNode()
    if n > 1:
        fullFBTs[1] = [[]]
    for i in range(2, n):
        newFBTs = []
        for root in fullFBTs[i%2]:
            leaves =fetchAllLeaves(root)
            # For all leaves clone the tree and add the leaves
            # Possibly loop over the original tree
            # Once we reach a leaf we may add a pair to the newRoot
            # Maybe recurse on all the trees at the same time but use an index to track the
            # cloned tree being updated
        fullFBTs[i] = newFBTs

    return fullFBTs[-1]