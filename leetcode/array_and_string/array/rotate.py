#URL: https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/
#Description
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve 
this problem.
Could you do it in-place with O(1) extra space?
"""

def rotateRightOnce(nums):
  l = len(nums)
  if l < 2:
    return
  else:
    temp = nums[l-1]
    for i in range(l-1, 0, -1):
      nums[i] = nums[i-1]
    nums[0] = temp


def rotateRight(nums, numRot):
  l = len(nums)
  if l < 2:
    return
  else:
    assert l > numRot
    temp = nums[l-numRot:]
    for i in range(l-1, numRot - 1, -1):
      nums[i] = nums[i-numRot]
    for i in range(len(temp)):
      nums[i] = temp[i]


def rotate(nums, k):
  l = len(nums)
  if l < 2:
    return
  else:
    numRot = k % l
    rotateRight(nums, numRot)
    # for i in range(numRot):
    #   rotateRightOnce(nums)
  
