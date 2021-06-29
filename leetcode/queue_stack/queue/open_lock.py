#URL: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/
#Description
"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', 
'3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can 
turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the 
wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum 
total number of turns required to open the lock, or -1 if it is impossible.


Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> 
"0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".


Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".


Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.


Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

def getNeighbours(lock):
  neighbours = set()
  lockNums = []
  for l in lock:
    lockNums.append(int(l))
  
  for i in range(len(lockNums)):
    lockVal = lockNums[i]
    clonedLock = lockNums[:]
    # Increase
    incVal = (lockVal + 1)%10
    clonedLock[i] = incVal
    neighbours.add("".join(str(l) for l in clonedLock))  
    # Decrease
    decVal = 9 if lockVal == 0 else lockVal - 1
    clonedLock[i] = decVal
    neighbours.add("".join(str(l) for l in clonedLock))
  
  return neighbours


def filterDeadends(neighbours, deadends):
  for d in deadends:
    if d in neighbours:
      neighbours.remove(d)


def filterVisited(neighbours, visited):
  for n in list(neighbours):
    if n in visited:
      neighbours.remove(n)


def searchLock(initLock, deadends, target):
  depth = 0
  visited = set()
  lockQueue = {initLock}
  while len(lockQueue) > 0:
    currentLevelLocks = list(lockQueue)
    lockQueue.clear()
    for lock in currentLevelLocks:
      visited.add(lock)
      if lock == target:
        return depth
      neighbours = getNeighbours(lock)
      filterDeadends(neighbours, deadends)
      filterVisited(neighbours, visited)
      lockQueue.update(neighbours)
    depth += 1
  return -1


def openLock(deadends, target):
  initLock = "".join('0' for t in target)
  if initLock in deadends:
    return -1
  
  return searchLock(initLock, deadends, target)