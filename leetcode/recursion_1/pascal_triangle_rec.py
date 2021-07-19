#URL: https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/
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
def getRowRecursive(depth, prevRow, rowIndex):
  currRow = [1 for i in range(depth + 1)]
  for i in range(1, depth):
    currRow[i] = prevRow[i-1] + prevRow[i]
  if depth == rowIndex:
    return currRow
  else:
    return getRowRecursive(depth + 1, currRow, rowIndex)


def getRow(rowIndex):
  assert rowIndex >= 0
  if rowIndex == 0:
    return [1]
  elif rowIndex == 1:
    return [1, 1]
  else:
    return getRowRecursive(2, [1,1], rowIndex)