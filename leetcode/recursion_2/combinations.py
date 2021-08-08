#URL: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2798/
#Description
"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.


Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
def combine_backtrack(start, end, k, nums, currCombi, allCombinations):
  if k == 0:
    allCombinations.append(currCombi[:])
    return
  for i in range(start, end):
    if (start + k) > end:
      return
    currCombi.append(nums[i])
    combine_backtrack(i + 1, end, k - 1, nums, currCombi, allCombinations)
    currCombi.pop()


def combine(n, k):
  nums = [i for i in range(1, n + 1)]
  allCombinations = []
  currCombi = []
  combine_backtrack(0, n, k, nums, currCombi, allCombinations)
  return allCombinations