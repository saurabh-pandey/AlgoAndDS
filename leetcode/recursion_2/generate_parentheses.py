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
import pdb

def generateParenthesisRecursive(numOpen, numClose, sol, sols):
  if numOpen > numClose:
    return
  if numOpen == 0 and numClose == 0:
    sols.append("".join(sol))
    return
  if numOpen > 0:
    sol.append("(")
    numOpen -= 1
    generateParenthesisRecursive(numOpen, numClose, sol, sols)
  if numClose > numOpen:
    sol.append(")")
    numClose -= 1
    generateParenthesisRecursive(numOpen, numClose, sol, sols)
  

def generateParenthesis(n):
  #IDEAS
  # 1. Either use previous solutions to construct the current one
  # 2. Or count all permutations and discard all that are not well-formed.
  # 3. There is one constraint that num of left braces is always >= num of right braces
  #   3.1. Can we use just this constraint to solve this problem?
  # pdb.set_trace()
  sols = []
  sol = ["("]
  generateParenthesisRecursive(n-1, n, sol, sols)
  return sols