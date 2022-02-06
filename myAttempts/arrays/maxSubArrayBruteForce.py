import sys

def maxSubArray(arr):
  """Brute-Force algo [O(n^2)] for maximum subarray problem"""
  maxSubArr = []
  maxSum = -sys.maxsize -1
  for start in range(len(arr)):
    for end in range(start+1, (len(arr) +1)):
      subArr = arr[start:end]
      subArrSum = sum(subArr)
      if (maxSum < subArrSum):
        maxSum = subArrSum
        maxSubArr = subArr
  return (maxSum, maxSubArr)
