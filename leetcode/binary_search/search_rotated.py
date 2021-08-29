#URL: https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
#Description
"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.
length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...
, nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is 
in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""
def search_rotated(nums, target):
  l = len(nums)
  if l == 0:
    return -1
  pivot_index = 0
  for i in range(l - 1):
    if nums[i] > nums[i + 1]:
      pivot_index = i + 1
      break
  start = 0
  end = l
  while end >= start:
    mid = (start + end)//2
    num_index = (mid + pivot_index) % l
    if target == nums[num_index]:
      return num_index
    elif target < nums[num_index]:
      end = mid - 1
    else:
      start = mid + 1
  return -1