#URL: https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
#Description
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the 
latest version of your product fails the quality check. Since each version is developed based on 
the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a 
function to find the first bad version. You should minimize the number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:

1 <= bad <= n <= 231 - 1
"""
import random

class BadVersion:
  def __init__(self, n, bad_ver = None) -> None:
    if bad_ver is None:
      self._bad_version = random.randint(1, n + 1)
    else:
      self._bad_version = bad_ver
  
  def isBadVersion(self, v):
    return v >= self._bad_version
  
  def bad_version(self):
    return self._bad_version


def firstBadVersion(n, bad_ver):
  start = 1
  end = n + 1
  while start < end:
    mid = (start + end)//2
    if bad_ver.isBadVersion(mid):
      end = mid
    else:
      if bad_ver.isBadVersion(mid + 1):
        return mid + 1
      else:
        start = mid + 1
  
  return start
