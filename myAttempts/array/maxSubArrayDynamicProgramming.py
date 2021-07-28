import sys

def maxSubArray(arr):
  """Dynamic Programming algo [O(n)] for maximum subarray problem"""
  maxSubArr = []
  maxSum = -sys.maxsize -1
  sumSoFar = 0
  subArrSoFar = []
  for i in arr:
    sumSoFar += i
    subArrSoFar.append(i)
    if (maxSum < sumSoFar):
      maxSum = sumSoFar
      maxSubArr = subArrSoFar[:]
    if (sumSoFar <= 0):
      sumSoFar = 0
      del subArrSoFar[:]
  return (maxSum, maxSubArr)
