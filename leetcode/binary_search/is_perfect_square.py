#URL: https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
#Description
"""
Given a positive integer num, write a function which returns True if num is a perfect square else 
False.
Follow up: Do not use any built-in library function such as sqrt.


Example 1:

Input: num = 16
Output: true


Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
"""
def isPerfectSquare(num):
  if num == 0:
    return True
  
  start = 1
  end = 1 if num == 1 else num//2
  while start <= end:
    mid = (start + end)//2
    sq = mid * mid
    if sq == num:
      return True
    elif sq < num:
      start = mid + 1
    else: # sq > num
      end = mid - 1
  return False