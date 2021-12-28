#URL: https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
#Description
"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the 
array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]


Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

def nearestToTarget(arr, x):
  start = 0
  end = len(arr) - 1
  while start + 1 < end:
    mid = (start + end)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      start = mid
    else: # arr[mid] > x
      end = mid
  
  dist_start = abs(arr[start] - x)
  dist_end = abs(arr[end] - x)
  if dist_start == dist_end:
    if arr[start] <= arr[end]:
      return start
    else:
      return end
  elif dist_start < dist_end:
    return start
  else: # dist_start < dist_end
    return end
  

def findClosestElements(arr, k, x):
  sz = len(arr)
  if sz == 0 or k == 0:
    return []
  target = nearestToTarget(arr, x)
  i = target
  j = target
  while i > -1 and j < sz and j - i + 1 < k:
    if i == 0:
      j += 1
    elif j == sz - 1:
      i -= 1
    else:
      a = arr[i - 1]
      b = arr[j + 1]
      dist_a = abs(a - x)
      dist_b = abs(b - x)
      if dist_a == dist_b:
        if a <= b:
          i -= 1
        else:
          j += 1
      elif dist_a < dist_b:
        i -= 1
      else: # dist_a > dist_b
        j += 1

  closestElems = arr[i: j + 1]
  return closestElems