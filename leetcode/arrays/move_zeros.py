# URL: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
# Description
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""
def shiftLeftBy(nums, start, end, howMany):
  assert start < end
  assert start >= howMany
  for i in range(start, end):
    nums[i - howMany] = nums[i]
  for i in range(end - howMany, end):
    nums[i] = 0

def moveZeroes(nums):
  length = len(nums)
  if (length < 2):
    return
  
  consecutiveZeros = 0
  i = 0
  end = length
  while i < end:
    # print(f'START: i = {i}, end = {end}, nums = {nums}, consecutiveZeros = {consecutiveZeros}')
    if nums[i] == 0:
      consecutiveZeros += 1
    else:
      shiftLeftBy(nums, i, end, consecutiveZeros)
      end -= consecutiveZeros
      i -= consecutiveZeros
      consecutiveZeros = 0
    i += 1
    # print(f'END: i = {i}, end = {end}, nums = {nums}, consecutiveZeros = {consecutiveZeros}')