#URL: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
#Description
"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.


Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

def isValidSquare(board, location, size):
    x, y = location
    bound_x = x + size
    bound_y = y + size
    if bound_x > len(board):
        return False
    if bound_y > len(board[0]):
        return False
    for i in range(x, bound_x):
        for j in range(y, bound_y):
            if board[i][j] != 1:
                return False
    return True


def findSquares(size, seedSquares, board):
    squares = []
    for i,j in seedSquares:
        if isValidSquare(board, (i, j), size):
            squares.append((i, j))
    return squares


def countSquareSubmatrices(matrix):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    if n == 0:
        return 0
    squares = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                squares.append((i, j))
    num_squares = len(squares)
    for size in range(2, min(m, n) + 1):
        squares = findSquares(size, squares, matrix)
        if not squares:
            break
        num_squares += len(squares)
    return num_squares
