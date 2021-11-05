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
def check_nearby_duplicate(nums, start, mid, end, t):
    ref_val = nums[mid]
    for i in range(start, mid):
        if abs(nums[i] - ref_val) <= t:
            return True
    for i in range(mid + 1, end):
        if abs(nums[i] - ref_val) <= t:
            return True
    return False


def containsNearbyAlmostDuplicate(nums, k, t):
    l = len(nums)
    chunk_size = 2*k + 1
    start = 0
    end = chunk_size
    end = l if end > l else end
    print()
    while start < l:
        mid = (start + end)//2
        print(f"start = {start}, mid = {mid}, end = {end}")
        if check_nearby_duplicate(nums, start, mid, end, t):
            return True
        start += chunk_size
        end += chunk_size
        end = l if end > l else end
    return False