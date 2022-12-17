#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
# Description
"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:

Input: arr = [2,1]
Output: false


Example 2:

Input: arr = [3,5,5]
Output: false


Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
def validMountainArray(arr):
  length = len(arr)
  if length < 3:
    return False
  
  # If the array descends in the beginning then no
  if (arr[1] <= arr[0]):
    return False
  
  ascending = True
  for i in range(1, length):
    if arr[i] == arr[i-1]:
      return False
    if ascending and (arr[i] < arr[i-1]):
      ascending = False
    elif not ascending and (arr[i] > arr[i-1]):
      return False
  
  return not ascending