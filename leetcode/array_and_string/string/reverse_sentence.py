#URL: https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
#Description
"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at 
least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The 
returned string should only have a single space separating the words. Do not include any extra 
spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"


Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.


Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed 
string.


Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"


Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow up: Could you solve it in-place with O(1) extra space?
"""

def reverseWords(s):
  l = len(s)
  if l == 0:
    return s
  words = []
  wrd = ""
  for i in range(l):
    if s[i] == " ":
      if len(wrd) > 0:
        words.append(wrd)
        wrd = ""
    else:
      wrd += s[i]
  
  if len(wrd) > 0:
    words.append(wrd)
  
  # print(words)
  nWrds = len(words)
  if nWrds == 0:
    return ""
  
  start = 0
  end = nWrds - 1
  while start < end:
    temp = words[start]
    words[start] = words[end]
    words[end] = temp
    start += 1
    end -= 1
  
  rev_str = ""

  for i in range(nWrds - 1):
    rev_str += words[i] + " "
  rev_str += words[nWrds - 1]

  return rev_str
