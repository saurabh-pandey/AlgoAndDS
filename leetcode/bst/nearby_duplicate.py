#URL: https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1013/
#Description
"""

Given an integer array nums and two integers k and t, return true if there are two distinct indices 
i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true


Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true


Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


Constraints:

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
"""
import pdb

def check_in_chunk(chunk, t):
    for i in range(1, len(chunk)):
        diff = abs(chunk[i] - chunk[i - 1])
        if diff <= t:
            return True
    return False


def check_crossover(current, next, t):
    for i in range(1, len(current)):
        for j in range(0, min(i, len(next))):
            diff = abs(current[i] - next[j])
            if diff <= t:
                return True
    return False
        


def get_next_chunk(start, chunk_size, l):
    next_start = start + chunk_size
    next_end = next_start + chunk_size
    if next_end > l:
        next_end = l
    return (next_start, next_end)


def containsNearbyAlmostDuplicate(nums, k, t):
    l = len(nums)
    chunk_size = k + 1
    start = 0
    end = chunk_size if chunk_size < l else l
    curr_chunk = nums[start:end]
    curr_chunk.sort()
    if check_in_chunk(curr_chunk, t):
        return True
    next_start, next_end = get_next_chunk(start, end, l)
    while next_start < l:
        next_chunk = nums[next_start:next_end]
        next_chunk.sort()
        if check_in_chunk(next_chunk, t):
            return True
        if check_crossover(curr_chunk, next_chunk, t):
            return True
        curr_chunk = next_chunk
        next_start, next_end = get_next_chunk(next_start, next_end, l)
    
    return False

