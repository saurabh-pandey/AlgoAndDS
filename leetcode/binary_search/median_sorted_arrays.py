#URL: https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/
#Description
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two 
sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000


Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000


Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
def merge_sorted(nums1, nums2):
  l1 = len(nums1)
  l2 = len(nums2)
  nums = [0 for i in range(l1 + l2)]
  i = 0
  j = 0
  k = 0
  while i < l1 and j < l2:
    if nums1[i] <= nums2[j]:
      nums[k] = nums1[i]
      i += 1
    else:
      nums[k] = nums2[j]
      j += 1
    k += 1
  
  while i < l1:
    nums[k] = nums1[i]
    i += 1
    k += 1
  
  while j < l2:
    nums[k] = nums2[j]
    j += 1
    k += 1
  return nums

def merge_find_median(nums1, nums2):
  nums = merge_sorted(nums1, nums2)
  l = len(nums)
  if l % 2 == 0:
    i = l // 2
    return (nums[i - 1] + nums[i])/2
  else:
    i = l // 2
    return nums[i]


def findMedianSortedArrays(nums1, nums2):
  return merge_find_median(nums1, nums2)