#URL: https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1018/
#Description
"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element 
in the sorted order, not the kth distinct element.
Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers 
nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth 
largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth 
element.
"""
import bisect
# from bst.node import Node

import pdb

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0
    
    def toStr(self):
        return f"[val = {self.val}, count = {self.count}]"


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        # pdb.set_trace()
        self.root = None
        # for n in nums:
        #     if self.root is None:
        #         self.root = TreeNode(n)
        #         self.root.count = 1
        #     else:
        #         self._insert(self.root, n)
        self.nums.sort()


    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
                node.left.count = node.count + 1
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
                node.right.count = node.count
                # node.count += 1
            else:
                self._insert(node.right, val)
                # node.count += 1
            # If a node is added to the right sub-tree then root and left subtree count is incremented by 1
            # This seems bad need to think of a new approach
            nodes = [node]
            while nodes:
                currNode = nodes.pop(0)
                if currNode.val < val:
                    currNode.count += 1
                    if currNode.left:
                        nodes.append(currNode.left)
                    if currNode.right:
                        nodes.append(currNode.right)
    
    
    def add(self, val):
        it = bisect.bisect_left(self.nums, val)
        self.nums.insert(it, val)
        assert self.k <= len(self.nums)
        return self.nums[-self.k]
    
    
    def new_add(self, val):
        if self.root is None:
                self.root = TreeNode(val)
                self.root.count = 1
        else:
            self._insert(self.root, val)
        tree_list = []
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            tree_list.append(node.toStr())
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        print(tree_list)

        