#URL: https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/
#Description
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000


Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100


Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""
import math

def abs_power(x, n):
  abs_x = abs(x)
  exp = math.log10(abs_x)
  if exp.is_integer():
    pow = int(exp) * n
    return 10**pow
  else:
    result = abs_x
    pow = 1
    while pow*2 <= n:
      result = result*result
      pow *= 2
    
    for i in range(pow, n):
      result *= abs_x
    return result

def power(x, n):
  abs_pow = abs_power(x,n)
  if x < 0:
    if n%2 == 0:
      return abs_pow
    else:
      return -abs_pow
  else:
    return abs_pow

def myPow(x, n):
  if n == 0:
    return 1.0
  elif n < 0:
    calcPow = power(x, -n)
    return 1.0/calcPow
  else:
    return power(x, n)
