#URL: https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
#Description
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For 
example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a
[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this 
array.
You must decrease the overall operation steps as much as possible.


Example 1:

Input: nums = [1,3,5]
Output: 1


Example 2:

Input: nums = [2,2,2,0,1]
Output: 0


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.


Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
def findMin(nums):
  l = len(nums)
  assert l > 0
  if l == 1:
    return nums[0]
  if nums[0] < nums[l - 1]:
    return nums[0]
  start = 0
  end = l
  while start < end:
    mid = (start + end)//2
    if nums[mid] < nums[0]:
      end = mid
    else:
      if nums[mid + 1] < nums[mid]:
        return nums[mid + 1]
      else:
        start = mid + 1