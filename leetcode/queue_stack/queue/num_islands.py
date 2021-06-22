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
def getNeighbours(i, j, m, n):
  neighbours = []
  nextI = i + 1
  if nextI < m:
    neighbours.append((nextI, j))
  nextJ = j + 1
  if nextJ < n:
    neighbours.append((i, nextJ))
  return neighbours


def filterNeighbours(neighbours, grid):
  validNeighbours = []
  for n in neighbours:
    i, j = n
    if grid[i][j] == 1:
      validNeighbours.append(n)
  return validNeighbours


def searchLand(nodes):
  # Start BFS from these nodes to search for land and return when on found
  pass

def getIsland(i, j):
  # Given a new land do BFS to check its ends
  pass

"""
IDEA: Idea is to apply the following algo:
1. searchIsland
2. spanIsland
3. Repeat 1
4. If 3 doesn't find a new land then end
"""

def numIslands(grid):
  m = len(grid)
  if m == 0:
    return 0
  n = len(grid[0])

  nodes = [(0, 0)]
  leafNodes = []
  while len(nodes) > 0:
    leafNodes = nodes[:]
    nodes.clear()
    size = len(leafNodes)
    for it in range(size):
      i, j = leafNodes[it]
      neighbours = getNeighbours(i, j, m, n)
      validNeighbours = filterNeighbours(neighbours, grid)
      nodes.extend(validNeighbours)

