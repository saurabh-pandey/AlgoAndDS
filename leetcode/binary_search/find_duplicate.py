#URL: https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/
#Description
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] 
inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2


Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Example 3:

Input: nums = [1,1]
Output: 1


Example 4:

Input: nums = [1,1,2]
Output: 1


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or 
more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

def findDuplicate_bf(nums):
  l = len(nums)
  for i in range(l - 1):
    n = nums[i]
    for j in range(i + 1, l):
      if n == nums[j]:
        return n
  return None


def findDuplicate_n(nums):
  l = len(nums)
  marker = [False for i in range(l - 1)]
  for n in nums:
    if marker[n - 1]:
      return n
    marker[n - 1] = True



def findDuplicate(nums):
  # return findDuplicate_bf(nums)
  return findDuplicate_n(nums)