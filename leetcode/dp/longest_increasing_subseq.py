#URL: https://leetcode.com/problems/longest-increasing-subsequence/
#Description
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of 
the array [0,3,1,6,2,2,7].


Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4


Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
def longest_inc_subseq(nums):
    pass

#IDEAS
# A sorted array is trivial
# Reverse sorted is again trivial
# Brute-force seems to be exponential here
# Given a smaller sub-array can we get the solution to the one bigger array?
# How will the solution change?
