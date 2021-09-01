#URL: https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
#Description
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of 
a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
def fetchRange(nums, target, mid):
  l = len(nums)
  rng = []
  i = mid
  while i >= 0:
    if nums[i] == target:
      i -= 1
    else:
      break
  rng.append(i + 1)
  i = mid
  while i < l:
    if nums[i] == target:
      i += 1
    else:
      break
  rng.append(i - 1)
  return rng

def searchRange(nums, target):
  l = len(nums)
  if l == 0:
    return [-1, -1]
  
  start, end = 0, l - 1
  while start + 1 < end:
    mid = (start + end)//2
    if nums[mid] == target:
      return fetchRange(nums, target, mid)
    elif nums[mid] > target:
      end = mid - 1
    else: # nums[mid] < target
      start = mid + 1
  
  if nums[start] == target:
    return fetchRange(nums, target, start)
  if nums[end] == target:
    return fetchRange(nums, target, end)
  
  return [-1, -1]
