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
import bst.operations as bst

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return not node.left and not node.right


def clone(root):
    if not root:
        return None
    newRoot = TreeNode()
    newRoot.left = clone(root.left)
    newRoot.right = clone(root.right)
    return newRoot


def attachToLeaf(origNode, newNodes, index):
    newIndex = index
    if isLeaf(origNode):
        newNode = newNodes[index]
        newNode.left = TreeNode()
        newNode.right = TreeNode()
        newIndex += 1
    else:
        leftNodes = [n.left for n in newNodes]
        leftIndex = attachToLeaf(origNode.left, leftNodes, newIndex)
        rightNodes = [n.right for n in newNodes]
        rightIndex = attachToLeaf(origNode.right, rightNodes, leftIndex)
        newIndex = rightIndex
    return newIndex


def allPossibleFBT(n):
    if n % 2 == 0:
        return []
    fullFBTs = [TreeNode()]
    for i in range(2, n, 2):
        newFBTs = []
        numLeaves = i//2
        for root in fullFBTs:
            currentFBTs = [clone(root) for _ in range(numLeaves)]
            attachToLeaf(root, currentFBTs, 0)
            newFBTs.extend(currentFBTs)
        uniqueFBTs = {}
        for root in newFBTs:
            treeList = bst.toList(root)
            key = "".join(str(n) for n in treeList)
            if key not in uniqueFBTs:
                uniqueFBTs[key] = root
        fullFBTs = uniqueFBTs.values()
    return fullFBTs