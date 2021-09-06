#URL: https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/
#Description
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in 
the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
def intersection_bf(nums1, nums2):
  l1 = len(nums1)
  l2 = len(nums2)
  results = set()
  if l1 == 0 or l2 == 0:
    return results
  for n1 in nums1:
    if n1 not in results:
      for n2 in nums2:
        if n1 == n2:
          results.add(n1)
  return results

def find_num(nums, target):
  start = 0
  end = len(nums) - 1
  while start <= end:
    mid = (start + end)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      start = mid + 1
    else: # nums[mid] > target
      end = mid - 1
  return False

def intersection_nlgn(nums1, nums2):
  l1 = len(nums1)
  l2 = len(nums2)
  results = set()
  if l1 == 0 or l2 == 0:
    return results
  
  sorted_unq_nums1 = sorted(set(nums1))
  sorted_unq_nums2 = sorted(set(nums2))
  smaller = sorted_unq_nums1
  larger = sorted_unq_nums2
  if len(sorted_unq_nums1) > len(sorted_unq_nums2):
    smaller = sorted_unq_nums2
    larger = sorted_unq_nums1
  for n1 in smaller:
    if find_num(larger, n1):
      results.add(n1)
  return results



def intersection(nums1, nums2):
  # return intersection_bf(nums1, nums2)
  return intersection_nlgn(nums1, nums2)