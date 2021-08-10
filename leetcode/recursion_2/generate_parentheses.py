#URL: https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2772/
#Description
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed 
parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]


Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
def generateParenthesis(n):
  #IDEAS
  # 1. Either use previous solutions to construct the current one
  # 2. Or count all permutations and discard all that are not well-formed.
  pass