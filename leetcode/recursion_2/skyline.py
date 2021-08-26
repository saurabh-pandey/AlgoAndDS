#URL: https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/3006/
#Description
"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city 
when viewed from a distance. Given the locations and heights of all the buildings, return the 
skyline formed by these buildings collectively.
The geometric information of each building is given in the array buildings where buildings[i] = 
[lefti, righti, heighti]:
lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at 
height 0.
The skyline should be represented as a list of "key points" sorted by their x-coordinate in the 
form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the 
skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark 
the skyline's termination where the rightmost building ends. Any ground between the leftmost and 
rightmost buildings should be part of the skyline's contour.
Note: There must be no consecutive horizontal lines of equal height in the output skyline. For 
instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 
should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]


Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key 
points in the output list.


Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""
import pdb
from operator import itemgetter


def filterDuplicates(buildings):
  l = len(buildings)
  assert l > 0
  uniqueBuildings = [buildings[0]]
  for i in range(1, l):
    x1, x2, h = buildings[i]
    prevX1, prevX2, prevH = buildings[i - 1]
    if (x1 != prevX1) or (x2 != prevX2) or (h != prevH):
      uniqueBuildings.append(buildings[i])
  return uniqueBuildings


def getEndPoint(skyline, left):
  return skyline[-1][1] if len(skyline) > 0 else left[0][0]



def mergeSkyline(left, right, skyline):
  if len(left) == 0:
    skyline.extend(right)
    return
  if len(right) == 0:
    skyline.extend(left)
    return
  leftmostRight = right[0][0]
  rightmostLeft = left[-1][1]
  if leftmostRight >= rightmostLeft:
    skyline.extend(left)
    if leftmostRight > rightmostLeft:
      skyline.append([rightmostLeft, leftmostRight, 0])
    skyline.extend(right)
  else: # leftmostRight < rightmostLeft
    i = 0
    j = 0
    while i < len(left) and j < len(right):
      l1, l2, lh = left[i]
      r1, r2, rh = right[j]
      if r1 >= l2:
        if r1 > l2:
          skyline.append([getEndPoint(skyline, left), l2, lh])
        i += 1
      else: # r1 < l2
        if r1 > getEndPoint(skyline, left):
          skyline.append([getEndPoint(skyline, left), r1, lh])
        if r2 <= l2:
          if rh > lh:
            skyline.append([getEndPoint(skyline, left), r2, rh])
          else:
            skyline.append([getEndPoint(skyline, left), r2, lh])
          j += 1
          if r2 == l2:
            i += 1
        else: # r2 > l2
          if rh > lh:
            skyline.append([getEndPoint(skyline, left), l2, rh])
          else:
            skyline.append([getEndPoint(skyline, left), l2, lh])
          i += 1
    if j < len(right):
      ep = getEndPoint(skyline, left)
      if ep == right[j][0]:
        skyline.extend(right[j:])
      elif ep < right[j][1]:
        skyline.append([ep, right[j][1], right[j][2]])
        skyline.extend(right[j + 1:])
    if i < len(left):
      ep = getEndPoint(skyline, left)
      if ep == left[i][0]:
        skyline.extend(left[i:])
      elif ep < left[i][1]:
        skyline.append([ep, left[i][1], left[i][2]])
        skyline.extend(left[i + 1:])
    


def combineEqualHeight(skyline):
  i = 1
  while i < len(skyline):
    if skyline[i - 1][2] == skyline[i][2]:
      assert skyline[i][1] > skyline[i-1][1], skyline
      skyline[i-1][1] = skyline[i][1]
      skyline.pop(i)
    else:
      i += 1


def getSkylineRecursive(buildings, skyline):
  l = len(buildings)
  if l == 0:
    return
  if l == 1:
    skyline.append(buildings[0])
    return
  leftSkyline = []
  getSkylineRecursive(buildings[0:int(l/2)], leftSkyline)
  rightSkyline = []
  getSkylineRecursive(buildings[int(l/2):], rightSkyline)
  mergeSkyline(leftSkyline, rightSkyline, skyline)
  combineEqualHeight(skyline)


def getKeyPoints(skyline):
  keypoints = []
  for s in skyline:
    keypoints.append([s[0], s[2]])
  keypoints.append([skyline[-1][1], 0])
  return keypoints

def getSkylineBuildings(buildings):
  skylineBuildings = []
  l = len(buildings)
  assert l > 0
  clonedBuildings = buildings[:]
  clonedBuildings.sort(key=itemgetter(0,1,2))
  uniqueBuildings = filterDuplicates(clonedBuildings)
  # pdb.set_trace()
  getSkylineRecursive(uniqueBuildings, skylineBuildings)
  return skylineBuildings


def getSkyline(buildings):
  skylineBuildings = getSkylineBuildings(buildings)
  keypoints = getKeyPoints(skylineBuildings)
  return keypoints