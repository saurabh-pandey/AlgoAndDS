#URL: https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
#Description
"""
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each 
integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them 
to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
def findTargetSumRecursive(sz, nums, target, sum, i, mult):
  newSum = sum + (mult * nums[i])
  if i == sz:
    if target == sum:
      return 1
    return 0
  
  count = 0
  count += findTargetSumRecursive(sz, nums, target, newSum, i + 1, 1)
  count += findTargetSumRecursive(sz, nums, target, newSum, i + 1, -1)
  return count
  

def findTargetSumWays(nums, target):
  if len(nums) == 0:
    return 0
  
  sz = len(nums)
  countLeft = findTargetSumRecursive(sz, nums, 0, 0, 1)
  countRight = findTargetSumRecursive(sz, nums, 0, 0, -1)

  return countLeft + countRight
