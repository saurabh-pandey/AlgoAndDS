#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
# Description
"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the
integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]


Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned
list does not count as extra space.
"""
def findDisappearedNumbers_O_n_space(nums):
  length = len(nums)
  disapperedNums = []
  if length < 2:
    disapperedNums = nums.copy()
    return disapperedNums
  
  marker = [False for i in range(length)]
  for i in range(length):
    assert nums[i] <= length
    marker[nums[i] - 1] = True
  
  for i in range(length):
    if marker[i] == False:
      disapperedNums.append(i + 1)
  return disapperedNums

def findDisappearedNumbers_const_space(nums):
  length = len(nums)
  disapperedNums = []
  if length < 2:
    disapperedNums = nums.copy()
    return disapperedNums
  
  i = 0
  while i < length:
    assert nums[i] <= length
    if nums[i] != i + 1:
      if nums[nums[i] - 1] == nums[i]:
        i += 1
      else:
        temp = nums[nums[i] - 1]
        nums[nums[i] - 1] = nums[i]
        nums[i] = temp
    else:
      i += 1
  for i in range(length):
    if nums[i] != i + 1:
      disapperedNums.append(i + 1)
  return disapperedNums
