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


def kthSmallestDist_bin_search(nums, k):
  n = len(nums)
  total_dists = n * (n - 1)//2
  assert k <= total_dists, "k out-of-range"


def kthSmallestDistancePair(nums, k):
  # return kthSmallestDist_bf(nums, k)
  return kthSmallestDist_hashMap(nums, k)