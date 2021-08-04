#URL: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2804/
#Description
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two 
queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.


Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.


Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""
class Queen:
  def __init__(self, row, col, n):
    assert n > 0
    assert 0 <= row < n
    assert 0 <= col < n
    self.n = n
    self.row = row
    self.col = col
    self.hill_diag = self.getHillDiagCells(row, col)
    self.dale_diag = self.getDaleDiagCells(row, col)
  
  def getHillDiagCells(self, r, c):
    diagCells = set()
    i = r + 1
    j = c - 1
    while i < self.n and j >= 0:
      diagCells.add(i, j)
      i += 1
      j -= 1
    
    i = r - 1
    j = c + 1
    while i >= 0 and j < self.n:
      diagCells.add(i, j)
      i -= 1
      j += 1
    
    return diagCells
  
  def getDaleDiagCells(self, r, c):
    diagCells = set()
    i = r - 1
    j = c - 1
    while i >= 0 and j >= 0:
      diagCells.add(i, j)
      i -= 1
      j -= 1
    
    i = r + 1
    j = c + 1
    while i < self.n and j < self.n:
      diagCells.add(i, j)
      i += 1
      j += 1
    
    return diagCells
 


def underAttack(r, c, queens):
  for q in queens:
    if r == q.row:
      return True
    elif c == q.col:
      return True
    elif (r, c) in q.hill_diag:
      return True
    elif (r, c) in q.dale_diag:
      return True
  return False


def backtrack_n_queens(row, n):
  solutions = 0
  queens = []
  for col in range(n):
    if not underAttack(row, col):
      # add queen
      queens.append(Queen(row, col))
      if len(queens) == n:
        solutions += 1


def totalNQueens(n):
  return backtrack_n_queens(0, n)