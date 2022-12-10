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
from typing import List

def sort_squares_v1(nums: List[int]) -> List[int]:
    sorted_squares = [0 for i in range(len(nums))]
    partition = 0
    for i in range(len(nums)):
        partition = i
        if nums[i] >= 0:
            break
    
    if partition == 0:
        for i in range(len(nums)):
            sorted_squares[i] = nums[i] * nums[i]
        return sorted_squares
    
    pos_id = partition
    neg_id = partition - 1
    sq_id = 0
    while pos_id < len(nums) and neg_id >= 0:
        if nums[pos_id] <= abs(nums[neg_id]):
            sorted_squares[sq_id] = nums[pos_id] * nums[pos_id]
            pos_id += 1
        else:
            sorted_squares[sq_id] = nums[neg_id] * nums[neg_id]
            neg_id -= 1
        sq_id += 1
    while pos_id < len(nums):
        sorted_squares[sq_id] = nums[pos_id] * nums[pos_id]
        pos_id += 1
        sq_id += 1
    while neg_id >= 0:
        sorted_squares[sq_id] = nums[neg_id] * nums[neg_id]
        neg_id -= 1
        sq_id += 1
    return sorted_squares


def sort_squares_v2(nums):
    pos_sqs = []
    neg_sqs = []
    for n in nums:
        if n < 0:
            neg_sqs.append(n*n)
        else:
            pos_sqs.append(n*n)
    sorted_sqs = []
    i = 0
    j = len(neg_sqs) - 1
    while (i < len(pos_sqs)) and (j > -1):
        if pos_sqs[i] < neg_sqs[j]:
            sorted_sqs.append(pos_sqs[i])
            i += 1
        else:
            sorted_sqs.append(neg_sqs[j])
            j -= 1
    while i < len(pos_sqs):
        sorted_sqs.append(pos_sqs[i])
        i += 1
    while j >= 0:
        sorted_sqs.append(neg_sqs[j])
        j -= 1
    return sorted_sqs