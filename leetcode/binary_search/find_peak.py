#URL: https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
#Description
"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains 
multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.


Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.


Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index 
number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
def findPeakElement_v1(nums):
  l = len(nums)
  start = 0
  end = l - 1
  while start < end:
    mid = (start + end)//2
    if mid == 0:
      break
    elif mid == l - 1:
      break
    else:
      if nums[mid] > nums[mid - 1]:
        if nums[mid] > nums[mid + 1]:
          return mid
        else:
          start = mid + 1
      else:
        end = mid
  
  if l == 1:
    return 0
  elif l > 1:
    if nums[0] > nums[1]:
      return 0
    if nums[l - 1] > nums[l - 2]:
      return l - 1

  return -1


def findPeakElement_v2(nums):
  l = len(nums)
  if l == 0:
    return -1
  elif l == 1:
    return 0
  start = 0
  end = l - 1
  while start + 1 < end:
    mid = (start + end)//2
    if nums[mid] > nums[mid - 1]:
      if nums[mid] > nums[mid + 1]:
        return mid
      else:
        start = mid
    else:
      end = mid
  
  if nums[start] > nums[end]:
    return start
  elif nums[start] < nums[end]:
    return end
  return -1


def findPeakElement(nums, use_v1 = False):
  if use_v1:
    return findPeakElement_v1(nums)
  else:
    return findPeakElement_v2(nums)
  