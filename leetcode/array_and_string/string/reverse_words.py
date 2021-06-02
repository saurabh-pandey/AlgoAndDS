#URL: https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
#Description
"""
Given a string s, reverse the order of characters in each word within a sentence while still 
preserving whitespace and initial word order.


Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"


Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
def reverseWord(wrd):
  wrdLen = len(wrd)
  wrdLst = list(wrd)
  start = 0
  end = wrdLen - 1
  while start < end:
    temp = wrdLst[start]
    wrdLst[start] = wrdLst[end]
    wrdLst[end] = temp
    start += 1
    end -= 1
  
  revStr = ""
  for s in wrdLst:
    revStr += s
  return revStr
  

def reverseWords(s):
  strLen = len(s)
  if strLen < 2:
    return s
  else:
    words = []
    wrd = ""
    for c in s:
      if c == " ":
        if len(wrd) > 0:
          revWrd = reverseWord(wrd)
          words.append(revWrd)
          wrd = ""
      else:
        wrd += c
    if len(wrd) > 0:
      revWrd = reverseWord(wrd)
      words.append(revWrd)
    
    nWrds = len(words)
    if nWrds == 0:
      return ""
    
    rev_str = ""
    for i in range(nWrds - 1):
      rev_str += words[i] + " "
    rev_str += words[nWrds - 1]
    return rev_str