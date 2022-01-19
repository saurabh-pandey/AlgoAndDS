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
    i, j = location
    if i + size > len(board):
        return False
    if j + size > len(board[0]):
        return False
    size_i = i + size
    size_j = j + size
    for i in range(i, size_i):
        for j in range(j, size_j):
            if board[i][j] != 1:
                return False
    return True


def findSquares(size, seed, board):
    squares = []
    for i,j in seed:
        if isValidSquare(board, (i, j), size):
            squares.append((i, j))
    return squares


def countSquareSubmatrices(matrix):
    # Should we count all 1's. Store it in some dict. Next use neighbours to find bigger squares.
    # Every pass adds 1 row and 1 col for every grid point. We can check if all is 1. We might
    # shift by one. Do we just the previous iteration solutions for next?
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
    for size in range(2, min(m, n)):
        squares = findSquares(size, squares, matrix)
        if not squares:
            break
        num_squares += len(squares)
    return num_squares