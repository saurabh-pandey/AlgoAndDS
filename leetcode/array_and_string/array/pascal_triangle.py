#URL: https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
#Description
"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""

def generatePascalTriangle(numRows):
  if numRows == 0:
    return []
  
  pascalTriangle = [[1]]

  depth = len(pascalTriangle)
  while depth < numRows:
    newRow = [1 for i in range(depth + 1)]
    for i in range(1, depth):
      newRow[i] = pascalTriangle[depth - 1][i - 1] + pascalTriangle[depth - 1][i]
    pascalTriangle.append(newRow)
    depth += 1
  return pascalTriangle