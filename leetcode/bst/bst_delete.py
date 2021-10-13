#URL: https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1006/
#Description
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.


Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.


Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.


Example 3:

Input: root = [], key = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
"""
import pdb

def findAndDeletePredecessor(node):
    prevNode = node
    currNode = node.left
    while currNode.right is not None:
        prevNode = currNode
        currNode = currNode.right
    if prevNode.left == currNode:
        prevNode.left = currNode.left
    else:
        prevNode.right = currNode.right
    return currNode.val

def findAndDeleteSuccessor(node):
    prevNode = node
    currNode = node.right
    while currNode.left is not None:
        prevNode = currNode
        currNode = currNode.left
    if prevNode.left == currNode:
        prevNode.left = currNode.left
    else:
        prevNode.right = currNode.right
    return currNode.val

def checkNodeAndDelete(node, is_pred = False):
    assert node is not None, f"Node {node.val} is set to None"
    if node.left is None and node.right is None:
        return None
    elif node.left is not None and node.right is not None:
        # Find predecessor (or successor), swap and then delete
        if is_pred:
            predVal = findAndDeletePredecessor(node)
            node.val = predVal
            return node
        else:
            succVal = findAndDeleteSuccessor(node)
            node.val = succVal
            return node
    elif node.left is not None and node.right is None:
        # Swap with left child and delete
        return node.left
    elif node.left is None and node.right is not None:
        # Swap with right child and delete
        return node.right


def deleteChildNode(node, key):
    if node.left is not None:
        if node.left.val == key:
            node.left = checkNodeAndDelete(node.left)
        else:
            deleteChildNode(node.left, key)
    if node.right is not None:
        if node.right.val == key:
            node.right = checkNodeAndDelete(node.right)
        else:
            deleteChildNode(node.right, key)

def deleteNode(root, key):
    # pdb.set_trace()
    if root is None:
        return None
    else:
        if root.val == key:
            newRoot = checkNodeAndDelete(root)
            return newRoot
        else:
            deleteChildNode(root, key)
            return root

            

    
