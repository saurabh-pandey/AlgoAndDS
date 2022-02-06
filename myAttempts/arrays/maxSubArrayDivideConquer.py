import sys

def subArraySum(arr):
  """A helper function for computing a part of cross-over case"""
  maxSum = -sys.maxsize -1
  sumSoFar = 0
  subArr = []
  for i in range(len(arr)):
    sumSoFar += arr[i]
    if (maxSum < sumSoFar):
      maxSum = sumSoFar
      subArr = arr[:i+1]
  return (maxSum, subArr)

def maxSubArrayCrossOver(left, right):
  """Computes cross-over case for maximum subarray problem.
  Used internally by Divide & Conquer algo.
  """
  maxLeft = subArraySum(list(reversed(left)))
  maxLeft[1].reverse()
  maxRight = subArraySum(right)
  return (maxLeft[0] + maxRight[0], maxLeft[1] + maxRight[1])

def maxSubArray(arr):
  """Divide & Conquer algo [O(nlgn)] for maximum subarray problem"""
  size = len(arr)
  if (size == 1):
    return (arr[0], arr)
  newSize = int(size/2)

  leftSubArr  = arr[:newSize]
  rightSubArr = arr[newSize:]

  leftResult   = maxSubArray(leftSubArr)
  rightResult  = maxSubArray(rightSubArr)
  crossOverRes = maxSubArrayCrossOver(leftSubArr, rightSubArr)
  return max(leftResult, rightResult, crossOverRes)
