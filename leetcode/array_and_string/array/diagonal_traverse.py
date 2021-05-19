#URL: https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
#Description
"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]


Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""

def findDiagonalOrder(mat):
  m = len(mat)
  if m == 0:
    return []
  n = len(mat[0])
  if n == 1:
    return mat
  # It seems every time we reach the end wall of matrix we slide in +ve side on that wall and then
  # continue along the diagonal
  # Also the general running pattern is we start with increasing i and decreasing j then once 
  # hitting the wall we switch to decreasing i and increasing j. Then again hitting the wall we 
  # switch and this goes on till we reach the last element in matrix.
  diagArr = []
  i = 0
  j = 0
  # Start with increasing i and decreasing j
  inc_i_dec_j = True
  while i >= 0 and i <= m:
    while j >= 0 and j <= n:
      diagArr.append(mat[i][j])
      # if iWall:
      #   slide-along the wall and switch
      # if jWall:
      #   slide-along the wall and switch
      if inc_i_dec_j:
        i += 1
        j -= 1
