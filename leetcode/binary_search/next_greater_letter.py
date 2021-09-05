#URL: https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
#Description
"""
Given a characters array letters that is sorted in non-decreasing order and a character target, 
return the smallest character in the array that is larger than target.
Note that the letters wrap around.
For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"


Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"


Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"


Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"


Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
def get_unique(letters):
  l = len(letters)
  unq_letters = [letters[0]]
  i = 1
  while i < l:
    if letters[i - 1] != letters[i]:
      unq_letters.append(letters[i])
    i += 1
  return unq_letters


def nextGreatestLetter(letters, target):
  unq_letters = get_unique(letters)
  l = len(unq_letters)
  start = 0
  end = l - 1
  while start < end:
    mid = (start + end)//2
    letter = unq_letters[mid]
    if letter == target:
      return unq_letters[mid + 1]
    elif letter < target:
      if target < unq_letters[mid + 1]:
        return unq_letters[mid + 1]
      else:
        start = mid + 1
    else:
      end = mid
  
  return unq_letters[0]