#URL: https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
#Description
"""
Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
def hit_min_wall(index, minLimit):
  return index < minLimit


def hit_max_wall(index, maxLimit):
  return index >= maxLimit


def findSpiralOrder(mat):
  m = len(mat)
  if m == 0:
    return []
  n = len(mat[0])

  matSize = m*n

  # Idea is to loop along the boundary. Each round will shrink the size of matrix by 2 in both
  # directions. Do this till we reach the end.
  # Seems like recursion could be a good idea here
  spiralArr = []

  i = 0
  j = 0

  increasing = True
  it_is_j = True
  minI = 0
  maxI = m - 1
  minJ = 0
  maxJ = n - 1

  while len(spiralArr) < matSize:
    assert i < m and j < n
    assert i >= 0 and j >= 0
    
    spiralArr.append(mat[i][j])

    if increasing:
      if it_is_j:
        j += 1
      else:
        i += 1
    else:
      if it_is_j:
        j -= 1
      else:
        i -= 1
    
    is_min_I_wall_hit = hit_min_wall(i, minI)
    is_min_J_wall_hit = hit_min_wall(j, minJ)
    is_max_I_wall_hit = hit_max_wall(i, maxI)
    is_max_J_wall_hit = hit_max_wall(j, maxJ)

    if is_max_J_wall_hit:
      # Time to move along increasing i
      it_is_j = False
      # One i row at the top done
      minI += 1
    elif is_max_I_wall_hit:
      # Time to move along decreasing j
      it_is_j = True
      increasing = False
      # One j col at the right done
      maxJ -= 1
    elif is_min_J_wall_hit:
      # Time to move along decreasing i
      it_is_j = False
      increasing = False
      # One i row at the bottom is done
      maxI -= 1
    elif is_min_I_wall_hit:
      # Time to move along increasing j
      it_is_j = True
      increasing = True
      # One j col at the left is done
      minJ += 1