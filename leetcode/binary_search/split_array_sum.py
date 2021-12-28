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
def cummulative_sum(nums):
  sums = [0 for _ in nums]
  sums[0] = nums[0]
  for i in range(1, len(nums)):
    sums[i] = sums[i - 1] + nums[i]
  return sums


def get_sum(sums, start, end):
  if start == 0:
    return sums[end - 1]
  else:
    return sums[end - 1] - sums[start - 1]


def findPartialSums(sums, partitions):
  partialSums = [0 for i in range(len(partitions) + 1)]
  bounds = []
  bounds.extend(partitions)
  bounds.append(len(sums))
  partialSums[0] = get_sum(sums, 0,partitions[0])
  for i in range(1, len(bounds)):
    partialSums[i] = get_sum(sums, bounds[i - 1], bounds[i])
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
  m = len(partitions)
  i = m - 1
  while i >= 0:
    part = partitions[i]
    maxPartVal = n - m + i
    if part < maxPartVal:
      partitions[i] += 1
      break
    i -= 1
  for j in range(i + 1, m):
    partitions[j] = partitions[j - 1] + 1


def splitArray_iterative(nums, m):
  n = len(nums)
  partitions = [(i + 1) for i in range(m - 1)]
  sums = cummulative_sum(nums)
  minSum = sums[-1]
  while isValidPartition(partitions, n):
    partialSums = findPartialSums(sums, partitions)
    maxPartSum = 0
    for ps in partialSums:
      maxPartSum = ps if ps > maxPartSum else maxPartSum
    minSum = maxPartSum if maxPartSum < minSum else minSum
    nextPartition(partitions, n)
  return minSum


def splitArray_recursive_impl(sums, m, part, start, max_sum, min_sum):
  end = len(sums) - m + part + 1
  if part == m - 1:
    nums_sum = get_sum(sums, start, end)
    max_sum = nums_sum if nums_sum > max_sum else max_sum
    min_sum = max_sum if max_sum < min_sum else min_sum
  elif part < m - 1:
    for i in range(start + 1, end + 1):
      nums_sum = get_sum(sums, start, i)
      max_sum = nums_sum if nums_sum > max_sum else max_sum
      min_sum = splitArray_recursive_impl(sums, m, part + 1, i, max_sum, min_sum)
  return min_sum


def splitArray_recursive(nums, m):
  sums = cummulative_sum(nums)
  min_sum = sums[-1]
  return splitArray_recursive_impl(sums, m, 0, 0, 0, min_sum)


def checkFeasable(nums, m, mid):
  nums_sum = 0
  count = 1
  for n in nums:
    nums_sum += n
    if nums_sum > mid:
      count += 1
      nums_sum = n
      if count > m:
        return False
  return True


def splitArray_bin_search(nums, m):
  min_sum = max(nums)
  max_sum = sum(nums)
  start = min_sum
  end = max_sum
  if m == 1:
    return max_sum
  while start < end:
    mid = start + (end - start)//2
    if checkFeasable(nums, m, mid):
      end = mid
    else:
      start = mid + 1
  return end


def splitArray(nums, m):
  # return splitArray_iterative(nums, m)
  # return splitArray_recursive(nums, m)
  return splitArray_bin_search(nums, m)
