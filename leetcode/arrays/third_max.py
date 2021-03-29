#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
# Description
"""
Given integer array nums, return the third maximum number in this array. If the third maximum does
not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.


Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.


Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
 

Constraints:

1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Can you find an O(n) solution?
"""
def thirdMax(nums):
  length = len(nums)
  if length == 0:
    return None
  
  max_0 = nums[0]
  for i in range(1, length):
    max_0 = nums[i] if nums[i] > max_0 else max_0
  
  if length < 3:
    return max_0
  
  minVal = -2**31 - 1
  max_1 = minVal
  for i in range(length):
    if nums[i] == max_0:
      continue
    max_1 = nums[i] if nums[i] > max_1 else max_1
  
  max_2 = minVal
  for i in range(length):
    if nums[i] == max_0:
      continue
    if nums[i] == max_1:
      continue
    max_2 = nums[i] if nums[i] > max_2 else max_2

  if max_2 == minVal:
    return max_0
  else:
    return max_2