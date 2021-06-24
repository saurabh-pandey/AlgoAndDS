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
import pdb

from collections import namedtuple

GridPoint = namedtuple('GridPoint', ['i', 'j'])

def getBounds(grid):
  m = len(grid)
  if m == 0:
    return (m,)
  n = len(grid[0])
  return (m, n)

def getAllNeighbours(node, bounds, visited):
  neighbours = []
  m, n = bounds
  i, j = node

  prevI = i - 1
  if prevI >= 0:
    if not visited[prevI][j]:
      neighbours.append(GridPoint(prevI, j))
  
  nextI = i + 1
  if nextI < m:
    if not visited[nextI][j]:
      neighbours.append(GridPoint(nextI, j))
  
  prevJ = j - 1
  if prevJ >= 0:
    if not visited[i][prevJ]:
      neighbours.append(GridPoint(i, prevJ))
  
  nextJ = j + 1
  if nextJ < n:
    if not visited[i][nextJ]:
      neighbours.append(GridPoint(i, nextJ))

  return neighbours


def getNeighbours(node, bounds):
  neighbours = []
  m, n = bounds
  i, j = node
  
  nextI = i + 1
  if nextI < m:
    neighbours.append(GridPoint(nextI, j))
  
  nextJ = j + 1
  if nextJ < n:
      neighbours.append(GridPoint(i, nextJ))

  return neighbours


def isLand(node, grid):
  return grid[node.i][node.j] == "1"


def isVisited(node, visited):
  return visited[node.i][node.j]


def filterNeighbours(neighbours, grid):
  validNeighbours = []
  for n in neighbours:
    if isLand(n, grid):
      validNeighbours.append(n)
  return validNeighbours


def spanIsland(node, bounds, grid, visited):
  assert isLand(node, grid) == True
  nodes = {node}
  leafNodes = {}
  while len(nodes) > 0:
    leafNodes = nodes.copy()
    nodes.clear()
    for it in leafNodes:
      assert isLand(it, grid) == True
      visited[it.i][it.j] = True
      neighbours = getAllNeighbours(it, bounds, visited)
      validNeighbours = filterNeighbours(neighbours, grid)
      nodes.update(validNeighbours)

def exploreGrid(node, bounds, grid, visited):
  nodes = {node}
  leafNodes = {}
  numIs = 0
  while len(nodes) > 0:
    leafNodes = nodes.copy()
    nodes.clear()
    for it in leafNodes:
      if not isVisited(it, visited) and isLand(it, grid):
        numIs += 1
        spanIsland(it, bounds, grid, visited)
      visited[node.i][node.j] = True
      neighbours = getNeighbours(it, bounds)
      nodes.update(neighbours)
  return numIs


def numIslands(grid):
  # pdb.set_trace()
  bounds = getBounds(grid)
  if bounds[0] == 0:
    return 0
  if bounds[1] == 0:
    return 0
  m, n = bounds
  visited = [[False for j in range(n)] for i in range(m)]

  rootNode = GridPoint(0, 0)
  return exploreGrid(rootNode, bounds, grid, visited)
