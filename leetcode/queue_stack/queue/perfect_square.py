#URL: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
#Description
"""
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product 
of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are 
not.


Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.


Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
# import pdb
import math

def numSquaresGreedy(n):
  assert n >= 0
  numPerfectSqrs = math.floor(math.sqrt(n))
  perfectSqs = [i * i for i in range(math.floor(math.sqrt(n)), 0, -1)]

  sqId = 0
  sum = 0
  squareSequence = []
  while sum < n and sqId < numPerfectSqrs:
    currSq = perfectSqs[sqId]
    newSum = sum + currSq
    if newSum > n:
      sqId += 1
    else:
      sum = newSum
      squareSequence.append(currSq)
  
  return squareSequence

def isPerfectSquare(n):
  sqrt = math.sqrt(n)
  intSqrt = int(sqrt)
  intSq = intSqrt*intSqrt
  return n == intSq


def numSquares(n):
  # pdb.set_trace()
  assert n >= 0
  sol = [1,2,3,1]
  for num in range(5, n + 1):
    if isPerfectSquare(num):
      sol.append(1)
    else:
      part = 1
      minNumSqs = num
      while part <= int(num/2):
        otherPart = num - part
        numSqs = sol[part - 1] + sol[otherPart - 1]
        minNumSqs = numSqs if numSqs < minNumSqs else minNumSqs
        part += 1
      sol.append(minNumSqs)
  return sol[n - 1]
