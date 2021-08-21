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


def filterNonParticipating(buildings):
  l = len(buildings)
  assert l > 0
  participatingBuildings = []
  for i in range(l):
    pass
  return participatingBuildings


def mergeSkyline(left, right, skyline):
  if len(left) == 0:
    skyline.extend(right)
    return
  if len(right) == 0:
    skyline.extend(left)
    return
  # l1, l2, lh = left[-1]
  skyline.extend(left)
  i = 0
  while i < len(right):
    r1, r2, rh = right[i]
    l1, l2, lh = skyline[-1]
    if r1 > l2:
      skyline.append([l2, r1, 0])
      break
    elif r1 <= l2:
      if lh > rh:
        #Case 1
        pass
      elif lh == rh:
        #Case 2
        pass
      else:
        #Case rh > lh
        pass
    


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


def splitbuildings(buildings):
  pass

def getSkylineD_C(buildings):
  # even split buildings[0:n/2] and buildings[n/2:]
  # stop at length 1
  # Now create skyline with a list [x1, x2, h]
  # Finally merge skylines 
  pass

def getSkyline(buildings):
  skyline = []
  #IDEAS
  # 1. Find all corners and check if they are inside or outside
  # 2. Case 1: Both outside means they are part of silhouette
  # 3. Case 2: One outside means they are intersection and out pt are used
  # 4. Case 3: Both inside means ignore

  # Another idea is as follows:
  # - Filter all congruent buildings except one
  # - Filter all buildings completely inside the other as they don't participate in the skyline
  # - Also sort all building based on left, right and height
  # - Finally in D & C merge two skylines
  l = len(buildings)
  assert l > 0
  clonedBuildings = buildings[:]
  clonedBuildings.sort(key=itemgetter(0,1,2))
  uniqueBuildings = filterDuplicates(clonedBuildings)
  finalBuildings = filterNonParticipating(uniqueBuildings)
  # Now it seems we can apply some algo (D & C ?) to solve
  return skyline