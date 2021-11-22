#URL: https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1057/
#Description
"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < 
n.


Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.


Example 2:

Input: nums = [0]
Output: 0


Example 3:

Input: nums = [2,4]
Output: 6


Example 4:

Input: nums = [8,10,2]
Output: 10


Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
"""
class TrieNode:
    def __init__(self) -> None:
        self.children = [None, None]
        self.isAdded = False
    
    def insert(self, state):
        # index = int(state)
        index = state
        if self.children[index]:
            return self.children[index]
        new_node = TrieNode()
        self.children[index] = new_node
        return new_node


def findMaximumXOR_bf(nums):
    l = len(nums)
    max_xor = 0
    for i in range(l):
        for j in range(i + 1, l):
            xor = nums[i] ^ nums[j]
            if xor > max_xor:
                max_xor = xor
    return max_xor




def findMaximumXOR(nums):
    trie_root = TrieNode()
    for n in nums:
        bits = [int(b) for b in bin(n)[2:]]
        curr_node = trie_root
        for bit in bits:
            curr_node = curr_node.insert(bit)
        curr_node.isAdded = True
    
    for n in nums:
        bits = [int(b) for b in bin(n)[2:]]
        inverted_bits = [int(not b) for b in bits]
        i = 0
        while i < len(bits):
            if trie_root.children[inverted_bits[i]]:
                pass
            elif trie_root.children[bits[i]]:
                pass