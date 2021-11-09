#URL: https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1015/
#Description
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node 
never differs by more than one.


Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from bst.node import Node

def createBST(nums, start, end):
    if start >= end:
        return None
    else:
        mid = (start + end)//2
        node = Node(nums[mid])
        node.left = createBST(nums, start, mid)
        node.right = createBST(nums, mid + 1, end)
        return node


def sortedArrayToBST(nums):
    return createBST(nums, 0, len(nums))