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
import bisect


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


def find_pairs_not_greater(sorted_nums, mid):
  num_pairs = 0
  for i in range(len(sorted_nums) - 1):
    partition = bisect.bisect_right(sorted_nums, sorted_nums[i] + mid, lo=i)
    num_pairs += (partition - i - 1)
  return num_pairs


def kthSmallestDist_bin_search(nums, k):
  n = len(nums)
  total_dists = n * (n - 1)//2
  assert k <= total_dists, "k out-of-range"
  sorted_nums = sorted(nums)
  min_dist = sorted_nums[1] - sorted_nums[0]
  max_dist = sorted_nums[-1] - sorted_nums[0]
  for i in range(2, n):
    dist = sorted_nums[i] - sorted_nums[i - 1]
    min_dist = dist if dist < min_dist else min_dist
    if min_dist == 0:
      break
  start = min_dist
  end = max_dist
  while start < end:
    mid = (start + end)//2
    num_pairs = find_pairs_not_greater(sorted_nums, mid)
    if num_pairs < k:
      start = mid + 1
    else:
      end = mid
  return start


def kthSmallestDistancePair(nums, k):
  # return kthSmallestDist_bf(nums, k)
  # return kthSmallestDist_hashMap(nums, k)
  return kthSmallestDist_bin_search(nums, k)