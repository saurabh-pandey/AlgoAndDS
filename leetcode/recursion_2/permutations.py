#URL: https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2903/
#Description
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the 
answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]


Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
def doPermute(nums, currPerm, perms):
  if len(currPerm) == len(nums):
    perms.append(currPerm[:])
    return
  for n in nums:
    if n not in currPerm:
      currPerm.append(n)
      doPermute(nums, currPerm, perms)
      currPerm.pop()



def permute(nums):
  perms = []
  currPerm = []
  doPermute(nums, currPerm, perms)
  return perms