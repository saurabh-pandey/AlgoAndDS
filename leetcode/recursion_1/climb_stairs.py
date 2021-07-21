#URL: https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/
#Description
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""
import math

def climbStairs(n):
  factorials = [1 for i in range(n+1)]
  for i in range(2, n+1):
    factorials[i] = i * factorials[i-1]
  
  sum = 0
  maxNumTwos = int(n/2)
  for i in range(maxNumTwos + 1):
    sum += factorials[n - i]/(factorials[n - 2*i] * factorials[i])
  
  return int(sum)