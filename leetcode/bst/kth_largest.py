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

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
    
    def toStr(self):
        return f"[val = {self.val}, count = {self.count}]"


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.root = None
        self.kth = None
        for n in nums:
            self.add(n)


    def _insert(self, node, val):
        node.count += 1
        if val <= node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
    

    def find_kth(self, node, k):
        if not node:
            return None
        
        if k > node.count:
            return None

        right_res = self.find_kth(node.right, k)
        if right_res:
            return right_res
        right_count = 0 if not node.right else node.right.count
        if k == (right_count + 1):
            return node
        else:
            new_k = k - right_count - 1
            return self.find_kth(node.left, new_k) 
        

    def toList(self):
        tree_list = []
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            tree_list.append(node.toStr())
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return tree_list
    
    
    def add(self, val):
        if self.kth and self.kth.val > val:
                return self.kth.val
        
        if self.root is None:
                self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
        
        if self.root.count < self.k:
            return None
        
        self.kth = self.find_kth(self.root, self.k)
        if self.kth:
            return self.kth.val
        else:
            return None
        