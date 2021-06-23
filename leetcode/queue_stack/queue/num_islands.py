#URL: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/
#Description
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return 
the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import namedtuple

GridPoint = namedtuple('GridPoint', ['i', 'j'])

def getBounds(grid):
  m = len(grid)
  if m == 0:
    return (m,)
  n = len(grid[0])
  return (m, n)

def getNeighbours(node, bounds, grid, visited):
  neighbours = []
  m, n = bounds
  i, j = node

  prevI = i - 1
  if prevI >= 0:
    if not visited[prevI][j]:
      neighbours.append((prevI, j))
  
  nextI = i + 1
  if nextI < m:
    if not visited[nextI][j]:
      neighbours.append((nextI, j))
  
  prevJ = j - 1
  if prevJ >= 0:
    if not visited[i][prevJ]:
      neighbours.append((i, prevJ))
  
  nextJ = j + 1
  if nextJ < n:
    if not visited[nextI][j]:
      neighbours.append((i, nextJ))

  return neighbours


def isLand(grid, i, j):
  return grid[i][j] == 1


def isWater(grid, i, j):
  return grid[i][j] == 0


def filterNeighbours(neighbours, grid):
  validNeighbours = []
  for n in neighbours:
    i, j = n
    if grid[i][j] == 1:
      validNeighbours.append(n)
  return validNeighbours


def searchIsland(node, bounds, grid, visited):
  # Start BFS from these nodes to search for land and return when one found
  nodes = [node]
  leafNodes = []
  while len(nodes) > 0:
    leafNodes = nodes[:]
    nodes.clear()
    size = len(leafNodes)
    for it in range(size):
      if isLand(grid, it[0], it[1]):
        visited[it[0]][it[1]] = True
        return it
      else:
        neighbours = getNeighbours(it, bounds, grid, visited)
        validNeighbours = filterNeighbours(neighbours, grid)
  return ()

  

def spanIsland(node, bounds, grid, visited):
  # Given a new land do BFS to check its ends
  nodes = [node]
  leafNodes = []
  while len(nodes) > 0:
    leafNodes = nodes[:]
    nodes.clear()
    size = len(leafNodes)
    for it in range(size):
      visited[it[0]][it[1]] = True
      neighbours = getNeighbours(it, bounds, grid, visited)
      validNeighbours = filterNeighbours(neighbours, grid)
  

"""
IDEA: Idea is to apply the following algo:
1. searchIsland
2. spanIsland
3. Repeat 1
4. If 3 doesn't find a new land then end
"""

def numIslands(grid):
  bounds = getBounds(grid)
  if bounds[0] == 0:
    return 0
  m, n = bounds
  visited = [[False for j in range(n)] for i in range(m)]

  numIs = 0
  seedNodes = [GridPoint(0, 0)]
  landNode = searchIsland(seedNodes, bounds, grid, visited)
  leafNodes = []
  while len(landNode) > 0:
    numIs += 1
    seedNodes = spanIsland(landNode)
    landNode = searchIsland(seedNodes)
  
  return numIs

