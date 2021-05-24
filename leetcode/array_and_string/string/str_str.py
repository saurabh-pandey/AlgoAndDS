#URL: https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
#Description
"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of 
haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an 
interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is
consistent to C's strstr() and Java's indexOf().


Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2


Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


Example 3:

Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""

def strStr(haystack, needle):
  szHay = len(haystack)
  szNdl = len(needle)
  if szNdl == 0:
    return 0
  else:
    for i in range(szHay - szNdl + 1):
      matchFound = True
      for j in range(szNdl):
        if haystack[i + j] != needle[j]:
          matchFound = False
          break
      if matchFound:
        return i
    return -1

