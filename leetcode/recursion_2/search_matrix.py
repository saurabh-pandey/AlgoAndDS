#URL: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2872/
#Description
"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The 
matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 
target = 5
Output: true


Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 
target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
def getLargerBounds(start, mid, end):
  bounds = []
  sI, sJ = start
  eI, eJ = end
  mI, mJ = mid
  bounds.append(((sI, mJ), (mI, eJ)))
  bounds.append(((mI, sJ), (eI, mJ)))
  bounds.append(((mI, mJ), (eI, eJ)))
  return bounds


def getSmallerBounds(start, mid, end):
  bounds = []
  sI, sJ = start
  eI, eJ = end
  mI, mJ = mid
  bounds.append(((sI, sJ), (mI, mJ)))
  bounds.append(((sI, mJ), (mI, eJ)))
  bounds.append(((mI, sJ), (eI, mJ)))
  return bounds


def searchMatrixRecursive(matrix, target, start, end):
  startI, startJ = start
  endI, endJ = end
  iSz = endI - startI
  jSz = endJ - startJ
  if iSz == 1 and jSz == 1:
    return matrix[startI][startJ] == target
  if iSz == 1 and jSz == 0:
    return matrix[startI][startJ] == target
  if iSz == 0 and jSz == 1:
    return matrix[startI][startJ] == target
  p = int((startI + endI)/2)
  q = int((startJ + endJ)/2)
  if matrix[p][q] == target:
    return True
  elif matrix[p][q] < target:
    # Ignore the top-left
    matBounds = getLargerBounds(start, (p,q), end)
    for bnd in matBounds:
      newStart, newEnd = bnd
      if searchMatrixRecursive(matrix, target, newStart, newEnd):
        return True
  else:
    # Ignore the bottom-right
    matBounds = getSmallerBounds(start, (p,q), end)
    for bnd in matBounds:
      newStart, newEnd = bnd
      if searchMatrixRecursive(matrix, target, newStart, newEnd):
        return True
  return False

def searchMatrix(matrix, target):
  m = len(matrix)
  if m == 0:
    return False
  n = len(matrix[0])
  if n == 0:
    return False
  return searchMatrixRecursive(matrix, target, (0, 0), (m,n))