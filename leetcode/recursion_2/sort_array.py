#URL: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/
#Description
"""
Given an array of integers nums, sort the array in ascending order.


Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]


Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
def merge(leftSortedArr, rightSortedArr):
  lIndex = 0
  rIndex = 0
  lSz = len(leftSortedArr)
  rSz = len(rightSortedArr)
  sortedArr = []
  while lIndex < lSz and rIndex < rSz:
    if leftSortedArr[lIndex] < rightSortedArr[rIndex]:
      sortedArr.append(leftSortedArr[lIndex])
      lIndex += 1
    else:
      sortedArr.append(rightSortedArr[rIndex])
      rIndex += 1

  sortedArr.extend(leftSortedArr[lIndex:])
  sortedArr.extend(rightSortedArr[rIndex:])
  return sortedArr


def mergeSortIterative(nums):
  sortedArrays = [[n] for n in nums]
  while len(sortedArrays) > 1:
    nextSortedArrays = []
    i = 0
    prevSz = len(sortedArrays)
    while i < (prevSz - 1):
      leftSortedArr = sortedArrays[i]
      rightSortedArr = sortedArrays[i + 1]
      sortedArr = merge(leftSortedArr, rightSortedArr)
      nextSortedArrays.append(sortedArr)
      i += 2
    if prevSz - i == 1:
      nextSortedArrays.append(sortedArrays[-1])
    sortedArrays = nextSortedArrays[:]
  return sortedArrays[0]


def mergeSortRecursive(nums):
  sz = len(nums)
  if sz < 2:
    return nums
  
  mid = int(sz/2)

  leftSortedArr = mergeSortRecursive(nums[:mid])
  rightSortedArr = mergeSortRecursive(nums[mid:])
  return merge(leftSortedArr, rightSortedArr)



def sortArray(nums, doIterative=False):
  if doIterative:
    return mergeSortIterative(nums)
  else:
    return mergeSortRecursive(nums)