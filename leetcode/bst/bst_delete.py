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
def findSuccessor(node):
    curr_node = node.right
    while curr_node.left is not None:
        curr_node = curr_node.left
    return curr_node


def deleteNode(root, key):
    parent_node = None
    curr_node = root
    while curr_node and curr_node.val != key:
        parent_node = curr_node
        if key < curr_node.val:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
    
    if curr_node is None:
        return root
    
    if curr_node.left is None and curr_node.right is None:
        if curr_node != root:
            if parent_node.left == curr_node:
                parent_node.left = None
            else:
                parent_node.right = None
            return root
        else:
            return None
    elif curr_node.left and curr_node.right:
        succ_node = findSuccessor(curr_node)
        val = succ_node.val
        deleteNode(curr_node, val)
        curr_node.val = val
        return root
    else:
        child = curr_node.left if curr_node.left else curr_node.right
        if curr_node != root:
            if parent_node.left == curr_node:
                parent_node.left = child
            else:
                parent_node.right = child
            return root
        else:
            return child
