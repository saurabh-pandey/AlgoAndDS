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
def findAndDeletePredecessor(node):
    prevNode = node
    currNode = node
    while currNode.right is not None:
        prevNode = currNode
        currNode = currNode.right
    prevNode.left = None
    return currNode.val

def findAndDeleteSuccessor(node):
    prevNode = node
    currNode = node
    while currNode.left is not None:
        prevNode = currNode
        currNode = currNode.left
    prevNode.left = None
    return currNode.val

def checkNodeAndDelete(node, is_pred = False):
    assert node is not None, f"Node {node.val} is set to None"
    if node.left is None and node.right is None:
        return None
    elif node.left is not None and node.right is not None:
        # Find predecessor (or successor), swap and then delete
        if is_pred:
            predVal = findAndDeletePredecessor(node.left)
            node.val = predVal
            return node
        else:
            succVal = findAndDeleteSuccessor(node.right)
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
            deleteChildNode(node.left)
    elif node.right is not None:
        if node.right.val == key:
            node.right = checkNodeAndDelete(node.right)
        else:
            deleteChildNode(node.right)

def deleteNode(root, key):
    if root is None:
        return None
    else:
        if root.val == key:
            newRoot = checkNodeAndDelete(root, key)
            return newRoot
        else:
            deleteChildNode(root, key)
            return root

            

    
