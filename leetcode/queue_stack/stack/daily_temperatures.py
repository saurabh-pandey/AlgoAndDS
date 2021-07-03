#URL: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
#Description
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer 
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]


Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]


Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from collections import defaultdict
import bisect

import pdb

def dailyTemperatures_on2(temperatures):
  answers = [0 for i in temperatures]
  tSz = len(temperatures)

  for i in range(tSz - 1):
    for j in range(i + 1, tSz):
      if temperatures[j] > temperatures[i]:
        answers[i] = j - i
        break
  return answers

def dailyTemperatures_using_map(temperatures):
  # pdb.set_trace()
  answers = [0 for i in temperatures]
  tSz = len(temperatures)
  
  tempIndicies = defaultdict(list)
  for i in range(tSz):
    tempIndicies[temperatures[i]].append(i)
  
  tempKeys = list(sorted(tempIndicies))

  for i in range(tSz - 1):
    keyId = bisect.bisect_left(tempKeys, temperatures[i])
    if keyId < len(tempKeys) - 1:
      minIndex = tSz
      for key in tempKeys[keyId+1 :]:
        minIndex = minIndex if tempIndicies[key][0] > minIndex else tempIndicies[key][0]
      if minIndex > i and minIndex < tSz:
        answers[i] = minIndex - i
    
    # remove this entry
    tempIndicies[tempKeys[keyId]].pop(0)
    if len(tempIndicies[tempKeys[keyId]]) == 0:
      del tempIndicies[tempKeys[keyId]]
      del tempKeys[keyId]

  return answers


def dailyTemperatures_using_stack(temperatures):
  # pdb.set_trace()
  answers = [0 for i in temperatures]
  tSz = len(temperatures)
  
  unresolvedTempStack = []
  for i in range(tSz):
    while len(unresolvedTempStack) > 0:
      topTempId = unresolvedTempStack[-1]
      if temperatures[i] > temperatures[topTempId]:
        answers[topTempId] = i - topTempId
        unresolvedTempStack.pop()
      else:
        break
    unresolvedTempStack.append(i)

  return answers


def dailyTemperatures(temperatures):
  return dailyTemperatures_using_stack(temperatures)
