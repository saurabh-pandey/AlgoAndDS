#URL: https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/
#Description
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true


Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true


Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
def containsNearbyDuplicate(nums, k):
    sz = len(nums)
    nums_map = {}
    for i in range(sz):
        n = nums[i]
        if n in nums_map:
            if ((i - nums_map[n][-1]) <= k):
                return True
            nums_map[n].append(i)
        else:
            nums_map[n] = [i]
    return False