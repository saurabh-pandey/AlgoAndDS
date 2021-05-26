#URL: https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
#Description:
"""
Write a function that reverses a string. The input string is given as an array of characters s.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
 

Follow up: Do not allocate extra space for another array. You must do this by modifying the input 
array in-place with O(1) extra memory.
"""
def swap(s, i , j):
  temp = s[i]
  s[i] = s[j]
  s[j] = temp

def reverseString(s):
  sLen = len(s)
  if sLen == 0:
    return
  else:
    i = 0
    j = sLen - 1
    while i < j:
      swap(s, i, j)
      i += 1
      j -= 1
