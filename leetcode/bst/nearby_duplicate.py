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
import bisect

import pdb

def check_in_chunk(chunk, t):
    for i in range(1, len(chunk)):
        diff = abs(chunk[i] - chunk[i - 1])
        if diff <= t:
            return True
    return False


def check_crossover(nums, current, next, t):
    curr_start, curr_end = current
    next_start, next_end = next
    for i in range(curr_start + 1, curr_end):
        for j in range(next_start, min(i, next_end)):
            diff = abs(nums[i] - nums[j])
            if diff <= t:
                return True
    return False
        


def get_next_chunk(start, chunk_size, l):
    next_start = start + chunk_size
    next_end = next_start + chunk_size
    if next_end > l:
        next_end = l
    return (next_start, next_end)


def containsNearbyAlmostDuplicate_slow(nums, k, t):
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
        # if check_crossover(nums[start:end], nums[next_start:next_end], t):
        if check_crossover(nums, (start,end), (next_start,next_end), t):
            return True
        curr_chunk = next_chunk
        start, end = next_start, next_end
        next_start, next_end = get_next_chunk(next_start, next_end, l)
    
    return False


def containsNearbyAlmostDuplicate_fast(nums, k, t):
    # pdb.set_trace()
    l = len(nums)
    chunk_size = k + 1
    start = 0
    end = chunk_size if chunk_size < l else l
    curr_chunk = nums[start:end]
    curr_chunk.sort()
    if check_in_chunk(curr_chunk, t):
        return True
    end += 1
    while end <= l:
        num_to_be_removed = nums[start]
        index = bisect.bisect_left(curr_chunk, num_to_be_removed)
        curr_chunk.pop(index)
        start += 1
        num_to_be_added = nums[end - 1]
        index = bisect.bisect_left(curr_chunk, num_to_be_added)
        curr_chunk.insert(index, num_to_be_added)
        if index < k:
            if abs(curr_chunk[index] - curr_chunk[index + 1]) <= t:
                return True
        if index > 0:
            if abs(curr_chunk[index - 1] - curr_chunk[index]) <= t:
                return True
        end += 1
    return False
    

def containsNearbyAlmostDuplicate(nums, k, t):
    # return containsNearbyAlmostDuplicate_slow(nums, k, t)
    return containsNearbyAlmostDuplicate_fast(nums, k, t)