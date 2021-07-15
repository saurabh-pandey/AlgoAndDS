#URL: https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
#Description
"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.


Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]


Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
def getValidNeighbours(node, distMat, bounds):
  neighbours = []
  m, n = bounds
  i, j = node
  posI = i + 1
  negI = i - 1
  posJ = j + 1
  negJ = j - 1

  if posI < m and distMat[posI][j] == -1:
    neighbours.append((posI, j))
  if negI >= 0 and distMat[negI][j] == -1:
    neighbours.append((negI, j))
  
  if posJ < n and distMat[i][posJ] == -1:
    neighbours.append((i, posJ))
  if negJ >= 0 and distMat[i][negJ] == -1:
    neighbours.append((i, negJ))
  
  return neighbours

def updateMatrix(mat):
  m = len(mat)
  if m == 0:
    return []
  n = len(mat[0])
  if n == 0:
    return [[]]
  
  bounds = (m, n)
  
  distMat = [[-1 for j in range(n)] for i in range(m)]
  
  # Init zero
  nodes = []
  for i in range(m):
    for j in range(n):
      if mat[i][j] == 0:
        distMat[i][j] = 0
        nodes.append((i,j))
  
  round = 1
  while len(nodes) > 0:
    currNodes = nodes[:]
    nodes.clear()
    for node in currNodes:
      for neighbour in getValidNeighbours(node, distMat, bounds):
        i, j = neighbour
        nodes.append(neighbour)
        distMat[i][j] = round
    round += 1
    

  return distMat
  