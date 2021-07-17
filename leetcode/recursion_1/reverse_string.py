#URL: https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/
#Description
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
def reverseStringRecursive(s, start, end):
  if start >= end:
    return
  reverseStringRecursive(s, start + 1, end - 1)
  
  temp = s[end]
  s[end] = s[start]
  s[start] = temp


def reverseString(s):
  reverseStringRecursive(s, 0, len(s) - 1)