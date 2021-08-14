#URL: https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2901/
#Description
"""
Given an array of integers heights representing the histogram's bar height where the width of each 
bar is 1, return the area of the largest rectangle in the histogram.


Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.


Example 2:

Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
def largestRectangle_bruteForce(heights):
  l = len(heights)
  maxArea = 0
  for i in range(l):
    currHeight = heights[i]
    minHeight = currHeight
    maxArea = currHeight if currHeight > maxArea else maxArea
    for j in range(i+1, l):
      minHeight = heights[j] if heights[j] < minHeight else minHeight
      newArea = minHeight * (j - i + 1)
      maxArea = newArea if newArea > maxArea else maxArea
  return maxArea


def largestRectangle_improved(heights):
  l = len(heights)
  maxArea = 0
  for i in range(l):
    currHeight = heights[i]
    if i != 0 and heights[i-1] == currHeight:
      continue
    currArea = heights[i]
    id = i - 1
    while id >= 0 and heights[id] >= currHeight:
      currArea += currHeight
      id -= 1
    id = i + 1
    while id < l and heights[id] >= currHeight:
      currArea += currHeight
      id += 1
    maxArea = currArea if currArea > maxArea else maxArea
  return maxArea


def largestRectangleArea(heights):
  # return largestRectangle_bruteForce(heights)
  return largestRectangle_improved(heights)