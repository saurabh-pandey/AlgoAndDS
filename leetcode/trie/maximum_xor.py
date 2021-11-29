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
import math


class TrieNode:
    def __init__(self) -> None:
        self.children = [None, None]
        self.isAdded = False
    
    def insert(self, state):
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


def convertToNumber(bits):
    result = 0
    l = len(bits)
    for i in range(l):
        result += bits[i] * 2**(l - i - 1)
    return result


def findMaximumXOR(nums):
    max_bits = 0
    for n in nums:
        num_bits = int(math.log2(n)) + 1 if n > 0 else 1
        if num_bits > max_bits:
            max_bits = num_bits
    # print(f"max_bits = {max_bits}")
    trie_root = TrieNode()
    max_bit_nums = []
    for n in nums:
        bits = [0 for _ in range(max_bits)]
        bin_bits = [int(b) for b in bin(n)[2:]]
        # print(f"For {n} bin_bits = {bin_bits}")
        for i in range(1, len(bin_bits) + 1):
            bits[-i] = bin_bits[-i]
        # print(f"For {n} bits = {bits}")
        # continue
        if bits[0] == 1:
            max_bit_nums.append(bits)
        curr_node = trie_root
        for bit in bits:
            curr_node = curr_node.insert(bit)
        curr_node.isAdded = True
    # return
    max_xor = 0
    xor_bits = [0 for _ in range(max_bits)]
    for bits in max_bit_nums:
        i = 0
        local_xor = 0
        isUsefulPath = True
        curr_node = trie_root
        while i < len(bits):
            bit = bits[i]
            inverse = int(not bit)
            next_node = curr_node.children[inverse]
            if next_node:
                xor_bits[i] = 1
            elif curr_node.children[bit]:
                next_node = curr_node.children[bit]
                if xor_bits[i] == 1:
                    # print(f"switching off xor_bits i = {i}")
                    isUsefulPath = False
                xor_bits[i] = 0
            curr_node = next_node
            i += 1
        local_xor = convertToNumber(xor_bits)
        if not isUsefulPath:
            if local_xor > max_xor:
                print(f"This should not be printed")
        if local_xor > max_xor:
            max_xor = local_xor
    return max_xor