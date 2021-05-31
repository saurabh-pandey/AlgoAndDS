#URL: https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
#Description
"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]


Example 2:

Input: rowIndex = 0
Output: [1]


Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

def getPascalTriangleRow(rowIndex):
  assert rowIndex >= 0
  if rowIndex == 0:
    return [1]
  elif rowIndex == 1:
    return [1, 1]
  else:
    prevRow = [1, 1]
    depth = 2
    while depth <= rowIndex:
      currRow = [1 for i in range(depth + 1)]
      for i in range(1, depth):
        currRow[i] = prevRow[i-1] + prevRow[i]
      prevRow = currRow
      depth += 1
    return prevRow
