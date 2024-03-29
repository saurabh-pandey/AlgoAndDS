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


def filterDegenerateBounds(bounds):
  filteredBounds = []
  for bound in bounds:
    (sI, sJ), (eI, eJ) = bound
    iSz = eI - sI
    jSz = eJ - sJ
    if iSz > 0 and jSz > 0:
      filteredBounds.append(bound)
  return filteredBounds


def searchMatrixRecursive(matrix, target, start, end):
  startI, startJ = start
  endI, endJ = end
  iSz = endI - startI
  jSz = endJ - startJ
  assert iSz != 0
  assert jSz != 0
  if iSz == 1 and jSz == 1:
    return matrix[startI][startJ] == target
  p = int((startI + endI)/2)
  q = int((startJ + endJ)/2)
  if matrix[p][q] == target:
    return True
  elif matrix[p][q] < target:
    # Ignore the top-left
    bounds = getLargerBounds(start, (p,q), end)
    matBounds = filterDegenerateBounds(bounds)
    for bnd in matBounds:
      newStart, newEnd = bnd
      if searchMatrixRecursive(matrix, target, newStart, newEnd):
        return True
  else:
    # Ignore the bottom-right
    bounds = getSmallerBounds(start, (p,q), end)
    matBounds = filterDegenerateBounds(bounds)
    for bnd in matBounds:
      newStart, newEnd = bnd
      if searchMatrixRecursive(matrix, target, newStart, newEnd):
        return True
  return False


def searchBoundingCol(matrix, target, start, end):
  si, sj = start
  ei, ej = end
  if sj == ej:
    return (True, False, None)
  mj = int((sj + ej)/2)
  minColVal = matrix[si][mj]
  maxColVal = matrix[ei - 1][mj]
  if target == minColVal:
    return (True, True, None)
  elif target < minColVal:
    return searchBoundingCol(matrix, target, start, (ei, mj))
  elif target == maxColVal:
    return (True, True, None)
  elif target > maxColVal:
    return searchBoundingCol(matrix, target, (si, mj + 1), end)
  else:
    return (False, False, mj)


def searchBoundingRows(matrix, target, col, rowBounds):
  si, ei = rowBounds
  for i in range(si, ei):
    matVal = matrix[i][col]
    if target == matVal:
      return (True, None)
    elif target < matVal:
      return (False, i)
  assert False, "Should not reach here"


def getTwoSearchBounds(start, end, row, col):
  bounds = []
  si, sj = start
  ei, ej = end
  i = row
  bounds.append(((si, col + 1), (i, ej)))
  bounds.append(((i, sj), (ei, col)))
  return bounds


def twoSearchRecursive(matrix, target, start, end):
  si, sj = start
  ei, ej = end
  iSz = ei - si
  jSz = ej - sj
  assert iSz != 0
  assert jSz != 0
  if target < matrix[si][sj]:
    return False
  if target > matrix[ei-1][ej-1]:
    return False
  if iSz == 1 and jSz == 1:
    return matrix[si][sj] == target
  
  found, res, col = searchBoundingCol(matrix, target, start, end)
  if found:
    return res
  
  found, row = searchBoundingRows(matrix, target, col, (si, ei))
  if found:
    return True

  twoSearchBnds = getTwoSearchBounds(start, end, row, col)
  matBounds = filterDegenerateBounds(twoSearchBnds)
  for bounds in matBounds:
    newStart, newEnd = bounds
    if twoSearchRecursive(matrix, target, newStart, newEnd):
      return True
  return False


def searchMatrix(matrix, target, useTwoSearch=True):
  m = len(matrix)
  if m == 0:
    return False
  n = len(matrix[0])
  if n == 0:
    return False
  if useTwoSearch:
    return twoSearchRecursive(matrix, target, (0, 0), (m,n))
  else:
    return searchMatrixRecursive(matrix, target, (0, 0), (m,n))
  