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
import pdb

def hit_min_wall(index):
  return index < 0


def hit_max_wall(index, limit):
  return index >= limit


def findDiagonalOrder(mat):
  # pdb.set_trace()
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
  # Start with decreasing i and increasing j
  dec_i_inc_j = True
  # while i >= 0 and i < m:
  #   while j >= 0 and j < n:
  while len(diagArr) < m*n:
    # NOTE: Precondition is that i and j are always withinn bounds
    diagArr.append(mat[i][j])
    if i == m - 1 and j == n - 1:
      print(f'Reached the last corner now breaking')
      i = m
      j = m
      break
    # if iWall:
    #   slide-along the wall and switch
    # if jWall:
    #   slide-along the wall and switch
    if dec_i_inc_j:
      i -= 1
      j += 1
    else:
      i += 1
      j -= 1
    
    is_min_I_wall_hit = hit_min_wall(i)
    is_min_J_wall_hit = hit_min_wall(j)
    is_max_I_wall_hit = hit_max_wall(i, m)
    is_max_J_wall_hit = hit_max_wall(j, n)
    
    # Corner cases
    if is_min_I_wall_hit and is_max_J_wall_hit:
      # Top right corner case
      i = 1
      j = n - 1
      dec_i_inc_j = False
    elif is_max_I_wall_hit and is_min_J_wall_hit:
      # Bottom left corner case
      j = 1
      i = m - 1
      dec_i_inc_j = True
    elif is_min_I_wall_hit and is_min_J_wall_hit:
      print(f'Min I and J corner case should not happen, i = {i} and j = {j}')
    elif is_max_I_wall_hit and is_max_J_wall_hit:
      print(f'Max I and J corner case should not happen, i = {i} and j = {j}')
    elif is_min_I_wall_hit:
      # Only hit a min I wall
      i = 0
      dec_i_inc_j = False
    elif is_max_I_wall_hit:
      # Only hit a max I wall
      i = m - 1
      j += 2
      dec_i_inc_j = True
    elif is_min_J_wall_hit:
      # Only hit a min J wall
      j = 0
      dec_i_inc_j = True
    elif is_max_J_wall_hit:
      # Only hit a min J wall
      j = n - 1
      i += 2
      dec_i_inc_j = False
    else:
      print(f'This case should be internal i = {i} and j = {j}')
  
  return diagArr
