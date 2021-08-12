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
    sol.pop()
    numOpen += 1
  if numClose > numOpen:
    sol.append(")")
    numClose -= 1
    generateParenthesisRecursive(numOpen, numClose, sol, sols)
    numClose += 1
    sol.pop()

def generateParenthesis(n):
  sols = []
  sol = ["("]
  generateParenthesisRecursive(n-1, n, sol, sols)
  return sols