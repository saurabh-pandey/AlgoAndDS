#URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
#Description
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true


Example 2:

Input: s = "()[]{}"
Output: true


Example 3:

Input: s = "(]"
Output: false


Example 4:

Input: s = "([)]"
Output: false


Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
def validParnePair(first, second):
  parenPair = (first, second)
  if parenPair == ('(', ')'):
    return True
  elif parenPair == ('{', '}'):
    return True
  elif parenPair == ('[', ']'):
    return True
  return False


def evaluate(stack, nextParen):
  if len(stack) == 0:
    stack.append(nextParen)
  else:
    topParen = stack[-1]
    if validParnePair(topParen, nextParen):
      stack.pop()
    else:
      stack.append(nextParen)


def isValid(s):
  parenStack = []
  for paren in s:
    evaluate(parenStack, paren)
  return len(parenStack) == 0