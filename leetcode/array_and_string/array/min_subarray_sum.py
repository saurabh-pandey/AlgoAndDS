#URL: https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
#Description
"""
Given an array of positive integers nums and a positive integer target, return the minimal length 
of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or 
equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1


Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time 
complexity is O(n log(n)).
"""


def minSubArrayLen_On(target, nums):
  l = len(nums)
  if l == 0:
    return 0
  else:
    sum = nums[0]
    minSubArrayL = l + 1
    subarrLen = 1
    startPtr = 0
    endPtr = 0
    while endPtr < l:
      if sum >= target:
        minSubArrayL = subarrLen if subarrLen < minSubArrayL else minSubArrayL
        if sum - nums[startPtr] >= target:
          sum -= nums[startPtr]
          startPtr += 1
          subarrLen -= 1
          minSubArrayL = subarrLen if subarrLen < minSubArrayL else minSubArrayL
        else:
          endPtr += 1
          if endPtr >= l:
            break
          sum += nums[endPtr]
          subarrLen += 1
      else:
        endPtr += 1
        if endPtr >= l:
          break
        sum += nums[endPtr]
        subarrLen += 1
    if minSubArrayL == l + 1:
      return 0
    else:
      return minSubArrayL

        


def minSubArrayLen_On2(target, nums):
  l = len(nums)
  if l == 0:
    return 0
  else:
    sum = 0
    for i in range(l):
      sum += nums[i]
    if sum < target:
      return 0
    
    minSubArrayL = l + 1
    for i in range(l):
      sum = 0
      subarrLen = 0
      for j in range(i, l):
        sum += nums[j]
        subarrLen += 1
        if sum >= target:
          minSubArrayL = subarrLen if subarrLen < minSubArrayL else minSubArrayL
          break
      if sum < target:
        break
          
    if minSubArrayL == l + 1:
      return 0
    else:
      return minSubArrayL



def minSubArrayLen(target, nums):
  # return minSubArrayLen_On2(target, nums)
  return minSubArrayLen_On(target, nums)
