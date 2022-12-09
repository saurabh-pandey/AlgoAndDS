#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
# Description
"""
Given a binary array, find the maximum number of consecutive 1s in this array.


Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.


Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
  max_count = 0
  count = 0
  for n in nums:
    if n == 1:
      count += 1
      max_count = count if count > max_count else max_count
    else:
      count = 0
  return max_count
