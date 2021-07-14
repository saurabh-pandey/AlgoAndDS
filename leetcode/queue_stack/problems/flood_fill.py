#URL: https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value 
of the image.
You are also given three integers sr, sc, and newColor. You should perform a flood fill on the 
image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to 
the starting pixel of the same color as the starting pixel, plus any pixels connected 
4-directionally to those pixels (also with the same color), and so on. Replace the color of all of 
the aforementioned pixels with newColor.
Return the modified image after performing the flood fill.


Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are 
colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the 
starting pixel.


Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""
def getNeighbours(node, baseColor, image, bounds):
  neighbours = []
  m,n = bounds
  i,j = node
  posI = i + 1
  negI = i - 1
  posJ = j + 1
  negJ = j - 1
  if posI < m and image[posI][j] == baseColor:
    neighbours.append((posI, j))
  if posJ < n and image[i][posJ] == baseColor:
    neighbours.append((i, posJ))
  if negI >= 0 and image[negI][j] == baseColor:
    neighbours.append((negI, j))
  if negJ >= 0 and image[i][negJ] == baseColor:
    neighbours.append((i, negJ))
  return neighbours

def floodFill(image, sr, sc, newColor):
  m = len(image)
  if m == 0:
    return image
  n = len(image[0])
  if n == 0:
    return image
  
  if sr >= m or sc >= n:
    return image
  
  if image[sr][sc] == newColor:
    return image
  
  bounds = (m,n)
  baseColor = image[sr][sc]
  nodes = [(sr,sc)]
  while len(nodes) > 0:
    currNode = nodes.pop(0)
    i,j = currNode
    if image[i][j] == newColor:
      continue
    image[i][j] = newColor
    for neighbour in getNeighbours(currNode, baseColor, image, bounds):
      nodes.append(neighbour)
  
  return image
