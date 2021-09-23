#URL: https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1042/
#Description
"""
Given an array nums which consists of non-negative integers and an integer m, you can split the 
array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.


Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.


Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9


Example 3:

Input: nums = [1,4,4], m = 3
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""
def findPartialSums(nums, partitions):
  partialSums = [0 for i in range(len(partitions) + 1)]
  bounds = [0]
  bounds.extend(partitions)
  bounds.append(len(nums))
  for i in range(len(bounds) - 1):
    sum = 0
    for j in range(bounds[i], bounds[i + 1]):
      sum += nums[i]
    partialSums[i] = sum
  return partialSums

def isValidPartition(partitions, n):
  if len(partitions) == 0:
    return False
  if partitions[-1] >= n:
    return False
  for i in range(len(partitions) - 1):
    if partitions[i + 1] <= partitions[i]:
      return False
  return True

def nextPartition(partitions, n):
  i = len(partitions) - 1
  while i >= 0:
    part = partitions[i]
    if part == n - 1:
      pass

def splitArray(nums, m):
  partitions = [(i + 1) for i in range(m - 1)]
  # sums = [0 for i in range(len(nums))]
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  #   sums[i] = sum
  minSum = sum
  while isValidPartition(partitions, len(nums)):
    partialSums = findPartialSums(nums, partitions)
    maxPartSum = 0
    for ps in partialSums:
      maxPartSum = ps if ps > maxPartSum else maxPartSum
    minSum = maxPartSum if maxPartSum < minSum else minSum
    nextPartition(partitions)
  return minSum

