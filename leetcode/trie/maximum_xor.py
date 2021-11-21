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
def findMaximumXOR(nums):
    """
    IDEA
    Seems like we need a Trie of bits for the numbers
    Generate the Trie
    Now maximum XOR with a number is possible if all it bits are reversed
    Given a number we start searching for a number with bits-reversed in the Trie
    We might want to start from the least-significant bit
    Keep looking for negated bits till we can find
    Max XOR possible with that number would be known
    Also, using Trie we are not comparing with all the remaining numbers
    Should we remove the number from Trie once we have seen with it?
    How do shrink search space as we march along the nums?
    Is it even needed?
    """
    l = len(nums)
    max_xor = 0
    for i in range(l):
        for j in range(i + 1, l):
            xor = nums[i] ^ nums[j]
            if xor > max_xor:
                max_xor = xor
    return max_xor