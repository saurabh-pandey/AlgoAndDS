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
import sys


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


def findMedianSortedArraysBinSearch(nums1, nums2):
  """
  Some ideas:
  1. Let m = len(nums1) and n = len(nums2)
  2. Let m <= n
  3. Now if m == 0 then median is in n only
  4. Median would be ~ (m + n)/2 index
  5. Let N = (m + n)/2
  6. Goal is to try to partition both the array such that:
    6.1. Total elements on the left of partition is N
    6.2. All left elements (in both arrays) are less than or equal to right elements
    6.3. Above would mean that suppose the partition is at x1, x2 in nums1 and y1, y2 in nums2 then 
    following inequality is true: x1 <= y2 and y1 <= x2
  7. In order to achieve above goal assume that all elements are from nums1 and if needed then from 
  nums2
  8. Now (7) would give the initial partition and from here onwards we start with the following 
  algo:
    8.1. start = 0, end = m - 1
    8.1. If (6.3) is not satisfied and start <= end
    8.2. mid = (start + end)/2 where start is start of left
  """
  m = len(nums1)
  n = len(nums2)
  X = nums1
  Y = nums2
  if m > n:
    X = nums2
    Y = nums1
  m = len(X)
  n = len(Y)
  if m == 0 and n == 0:
    return None
  elif m == 0:
    mid = n // 2
    if n % 2 == 0:
      return (Y[mid - 1] + Y[mid])/2
    else:
      return Y[mid]
  else:
    # Here m and n are not empty and m <= n
    total_len = m + n
    isSizeEven = total_len % 2 == 0
    N = total_len//2 if isSizeEven else (total_len + 1)//2
    x_part = N if N <= m else m
    y_part = 0 if N <= m else N - m
    start = 0
    end = x_part
    while start < end:
      x1 = None if x_part == 0 else nums1[x_part - 1]
      x2 = None if x_part == m else nums1[x_part]
      y1 = None if y_part == 0 else nums2[y_part - 1]
      y2 = None if y_part == n else nums2[y_part]
      x_part_valid = True
      if x1 is not None and y2 is not None:
        if x1 > y2:
          x_part_valid = False
      y_part_valid = True
      if x2 is not None and y1 is not None:
        if y1 > x2:
          y_part_valid = False
      # In this case we shrink X
      if not x_part_valid:
        mid = (start + end)//2
        x_part = mid
        y_part += end - mid
        end = mid
      # In this case we expand X
      if not y_part_valid:
        mid = (end + m)//2
        x_part = mid
        y_part -= end - mid
        end = mid
    
    # Once here we have a valid x_part and y_part
    minint = -sys.maxsize - 1
    maxint = sys.maxsize
    x1 = minint if x_part == 0 else nums1[x_part - 1]
    x2 = maxint if x_part == m else nums1[x_part]
    y1 = minint if y_part == 0 else nums2[y_part - 1]
    y2 = maxint if y_part == n else nums2[y_part]
    if isSizeEven:
      # Median is avg of max(x1, y1) and min(x2, y2)
      return (max(x1, y1) + min(x2, y2))/2
    else:
      # Median is avg of max(x1, y1)
      return max(x1, y1)




def findMedianSortedArrays(nums1, nums2):
  # return merge_find_median(nums1, nums2)
  return findMedianSortedArraysBinSearch(nums1, nums2)