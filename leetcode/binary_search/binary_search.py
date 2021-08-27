#URL: https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
#Description
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a 
function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
def searchRecursive(nums, start, end, target):
  assert len(nums) > 0
  size = end - start + 1
  if size == 0:
    return -1
  
  mid = (start + end)//2
  if target == nums[mid]:
    return mid
  elif target < nums[mid]:
    return searchRecursive(nums, start, mid - 1, target)
  else:
    return searchRecursive(nums, mid + 1, end, target)


def search(nums, target):
  l = len(nums)
  if l == 0:
    return -1
  return searchRecursive(nums, 0, l - 1, target)