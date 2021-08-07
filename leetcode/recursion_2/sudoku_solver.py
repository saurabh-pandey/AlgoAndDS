#URL: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/
#Description
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
def isCellFilled(board, cell):
  i, j = cell
  return board[i][j].isnumeric()


def nextCell(cell, n):
  i, j = cell
  if j == n - 1:
    if i == n - 1:
      return None
    else:
      return (i + 1, 0)
  else: # j < n - 1
    return (i, j + 1)


def getNextEmptyCell(board, start):
  n = len(board)
  nextC = nextCell(start, n)
  while nextC is not None:
    if not isCellFilled(board, nextC):
      return nextC
    nextC = nextCell(nextC, n)
  return None


def foundMatchingInRow(num, row, board):
  n = len(board)
  for i in range(n):
    if isCellFilled(board, (row, i)) and num == int(board[row][i]):
      return True
  return False


def findSubGrid(cell):
  subGridBounds = [((0, 0), (2, 2)), ((0, 3), (2, 5)), ((0, 6), (2, 8)),
                   ((3, 0), (5, 2)), ((3, 3), (5, 5)), ((3, 6), (5, 8)),
                   ((6, 0), (8, 2)), ((6, 3), (8, 5)), ((6, 6), (8, 8))]
  i, j = cell
  for subGrid in subGridBounds:
    (si, sj), (ei, ej) = subGrid
    if si <= i <= ei and sj <= j <= ej:
      return subGrid
  assert False, "Shouldn't reach here"



def foundMatchingInSubGrid(num, cell, board):
  subGrid = findSubGrid(cell)
  (si, sj), (ei, ej) = subGrid
  for i in range(si, ei + 1):
    for j in range(sj, ej + 1):
      if isCellFilled(board, (i, j)) and num == int(board[i][j]):
        return True
  return False    


def foundMatchingInCol(num, col, board):
  n = len(board)
  for i in range(n):
    if isCellFilled(board, (i, col)) and num == int(board[i][col]):
      return True
  return False


def isValid(num, cell, board):
  row, col = cell
  if foundMatchingInRow(num, row, board):
    return False
  elif foundMatchingInCol(num, col, board):
    return False
  elif foundMatchingInSubGrid(num, cell, board):
    return False
  return True


def solveSudokuBacktrack(board, cell):
  emptyCell = cell if not isCellFilled(board, cell) else getNextEmptyCell(board, cell)
  i, j = emptyCell
  for num in range(1, 10):
    if isValid(num, emptyCell, board):
      board[i][j] = str(num)
      nextEmptyCell = getNextEmptyCell(board, emptyCell)
      if nextEmptyCell == None:
        return True
      else:
        if solveSudokuBacktrack(board, nextEmptyCell):
          return True
        else:
          board[i][j] = "."
  return False


def solveSudoku(board):
  solveSudokuBacktrack(board, (0, 0))