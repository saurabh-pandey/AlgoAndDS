# URL: https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
# Description
"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.


Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.
"""

def shiftLeft(nums, start, end, count):
  assert start > count and start < end
  assert end <= len(nums)
  replacement = nums[start - 1]
  for i in range(start, end):
    nums[i - count] = nums[i]
  for i in range(end - count, end):
    nums[i] = replacement

"""
This function only guarantees the unique elements and all duplicates are shuffled beyond the new
length. Thus no element of the original array is overwritten.
"""
def removeDuplicatesRetainAll(nums):
  newLen = len(nums)
  if newLen < 2:
    return newLen
  # nums is 2 or more
  i = 1
  consecutiveDuplicateCount = 0
  end = newLen
  while i < end:
    if nums[i-1] == nums[i]:
      consecutiveDuplicateCount += 1
      newLen -= 1
    else:
      shiftLeft(nums, i, end, consecutiveDuplicateCount)
      i -= consecutiveDuplicateCount
      end -= consecutiveDuplicateCount
      consecutiveDuplicateCount = 0
    i += 1
  return newLen

"""
This function only guarantees the unique elements and anything beyond is overwritten
"""
def removeDuplicatesOverwrite(nums):
  length = len(nums)
  if length < 2:
    return length
  # nums is 2 or more
  writePos = 1
  for i in range(1, length):
    if nums[i - 1] != nums[i]:
      nums[writePos] = nums[i]
      writePos += 1
  return writePos

def removeDuplicates(nums, overwrite = True):
  # TODO: Ideally we should run same test for both overwrite True and False for full coverage
  if overwrite:
    return removeDuplicatesOverwrite(nums)
  else:
    return removeDuplicatesRetainAll(nums)