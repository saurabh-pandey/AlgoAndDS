#URL: https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
#Description
"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of 
the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or 
x ** 0.5.


Example 1:

Input: x = 4
Output: 2


Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is 
returned.
 

Constraints:

0 <= x <= 231 - 1
"""
import pdb

def mySqrtImpl(x, start, end):
  if end - start <= 1:
    sq_end = end * end
    if sq_end == x:
      return end
    else:
      return start
  mid = (start + end)//2
  sq_mid = mid * mid
  if sq_mid == x:
    return mid
  elif sq_mid > x:
    return mySqrtImpl(x, start, mid)
  else: # sq_mid < x
    return mySqrtImpl(x, mid, end)

  
def mySqrt(x):
  assert x >= 0
  if x == 0:
    return 0
  if x == 1:
    return 1
  # pdb.set_trace()
  return mySqrtImpl(x, 1, x)