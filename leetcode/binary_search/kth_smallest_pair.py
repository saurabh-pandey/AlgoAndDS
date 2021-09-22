#URL: https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1041/
#Description
"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs 
nums[i] and nums[j] where 0 <= i < j < nums.length.


Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.


Example 2:

Input: nums = [1,1,1], k = 2
Output: 0


Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""
import sys

import pdb
import time

def kthSmallestDist_bf(nums, k):
  n = len(nums)
  total_dists = n * (n - 1)//2
  assert k <= total_dists, "k out-of-range"
  dists = [0 for i in range(total_dists)]
  d_i = 0
  for i in range(n):
    for j in range(i + 1, n):
      dists[d_i] = abs(nums[i] - nums[j])
      d_i += 1
  dists.sort()
  return dists[k - 1]


def kthSmallestDist_hashMap(nums, k):
  n = len(nums)
  total_dists = n * (n - 1)//2
  assert k <= total_dists, "k out-of-range"
  dist_map = {}
  for i in range(n):
    for j in range(i + 1, n):
      dist = abs(nums[i] - nums[j])
      dist_map[dist] = dist_map.get(dist, 0) + 1
  # print(dist_map)
  counter = 0
  for dist in sorted(dist_map):
    counter += dist_map[dist]
    if k <= counter:
      return dist
  assert False, "Reached end"

# def get_cumlative_pairs_map(nums):
#   n = len(nums)
#   dist_map = {}
#   for i in range(n):
#     for j in range(i + 1, n):
#       dist = abs(nums[i] - nums[j])
#       dist_map[dist] = dist_map.get(dist, 0) + 1
#   cumlative_pairs_map = {}
#   cumlative_pairs = 0
#   for dist in sorted(dist_map):
#     cumlative_pairs += dist_map[dist]
#     cumlative_pairs_map[dist] = cumlative_pairs
#   return cumlative_pairs_map


def get_cumlative_pairs_map(nums):
  n = len(nums)
  unique_nums = {}
  for i in range(n):
    unique_nums[nums[i]] = unique_nums.get(nums[i], 0) + 1
  dist_map = {}
  u_nums = sorted(unique_nums)
  # print(f"Unique nums found = {u_nums}")
  for i in range(len(u_nums)):
    count = unique_nums[u_nums[i]]
    if count > 1:
      increment = count * (count - 1)//2
      dist_map[0] = dist_map.get(0, 0) + increment
    for j in range(i + 1, len(u_nums)):
      dist = abs(u_nums[i] - u_nums[j])
      increment = count * unique_nums[u_nums[j]]
      dist_map[dist] = dist_map.get(dist, 0) + increment
  # print(dist_map)
  cumlative_pairs_map = {}
  cumlative_pairs = 0
  for key in sorted(dist_map):
    cumlative_pairs += dist_map[key]
    cumlative_pairs_map[key] = cumlative_pairs
  return cumlative_pairs_map
  

def kthSmallestDist_bin_search(nums, k):
  n = len(nums)
  total_dists = n * (n - 1)//2
  assert k <= total_dists, "k out-of-range"
  # start = time.time()
  cumlative_pairs_map = get_cumlative_pairs_map(nums)
  # print(cumlative_pairs_map)
  # end = time.time()
  # print(f"Time = {end - start}")
  sorted_dists = sorted(cumlative_pairs_map)
  start = 0
  end = len(sorted_dists) - 1
  while start <= end:
    mid = (start + end)//2
    dist = sorted_dists[mid]
    num_pairs = cumlative_pairs_map[dist]
    if num_pairs == k:
      return dist
    elif num_pairs > k:
      if mid - 1 >= 0:
        prev_num_pairs = cumlative_pairs_map[sorted_dists[mid - 1]]
        if prev_num_pairs < k:
          return dist
      end = mid - 1
    else:
      start = mid + 1
  return sorted_dists[start]


def kthSmallestDistancePair(nums, k):
  # return kthSmallestDist_bf(nums, k)
  # return kthSmallestDist_hashMap(nums, k)
  return kthSmallestDist_bin_search(nums, k)