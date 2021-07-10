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
import pdb

add = lambda x, y: x + y
sub = lambda x, y: x - y

def checkTargetSumMatch(target, stackSum):
  targetSum = target + stackSum
  targetDiff = target - stackSum
  count = 0
  if targetSum == 0:
    count += 1
  if targetDiff == 0:
    count += 1
  return count


def findTargetSumRec(sz, nums, target, runningSum, stackSum, i, action):
  newStackSum = action(stackSum, nums[i])
  if i == sz - 1:
    return checkTargetSumMatch(target, newStackSum)
  
  sumRemainStack = runningSum[i + 1]
  maxPositiveSum = newStackSum + sumRemainStack
  minPositiveSum = newStackSum - sumRemainStack
  minNegativeSum = -newStackSum - sumRemainStack
  maxNegativeSum = -newStackSum + sumRemainStack
  isTargetInPosRange = (target <= maxPositiveSum) and (target >= minPositiveSum)
  isTargetInNegRange = (target <= maxNegativeSum) and (target >= minNegativeSum)
  if isTargetInPosRange or isTargetInNegRange:
    count = 0
    count += findTargetSumRec(sz, nums, target, runningSum, newStackSum, i + 1, add)
    count += findTargetSumRec(sz, nums, target, runningSum, newStackSum, i + 1, sub)
    return count
  else:
    return 0
  

def findTargetSumWays(nums, target):
  # pdb.set_trace()
  if len(nums) == 0:
    return 0
  
  sz = len(nums)
  nums.sort(reverse=True)
  runningSum = [sum(nums[i:]) for i in range(sz)]
  return findTargetSumRec(sz, nums, target, runningSum, 0, 0, add)
