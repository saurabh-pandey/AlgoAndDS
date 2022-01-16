#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
# Description
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

def sortedSquares(nums):
    sortedSquares = [0 for i in range(len(nums))]
    partition = 0
    for i in range(len(nums)):
        partition = i
        if nums[i] >= 0:
            break
    
    if partition == 0:
        for i in range(len(nums)):
            sortedSquares[i] = nums[i] * nums[i]
        return sortedSquares
    
    posId = partition
    negId = partition - 1
    sqId = 0
    while posId < len(nums) and negId >= 0:
        if nums[posId] <= abs(nums[negId]):
            sortedSquares[sqId] = nums[posId] * nums[posId]
            posId += 1
        else:
            sortedSquares[sqId] = nums[negId] * nums[negId]
            negId -= 1
        sqId += 1
    while posId < len(nums):
        sortedSquares[sqId] = nums[posId] * nums[posId]
        posId += 1
        sqId += 1
    while negId >= 0:
        sortedSquares[sqId] = nums[negId] * nums[negId]
        negId -= 1
        sqId += 1
    return sortedSquares