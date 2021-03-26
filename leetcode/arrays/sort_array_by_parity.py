# URL: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
# Description
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

 
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
def sortArrayByParity(A):
  length = len(A)
  if length == 0:
    return 0
  elif length == 1:
    if (A[0] % 2) == 0:
      return 1
    else:
      return 0

  evenOddPartition = 0
  for i in range(length):
    if (A[i] % 2) == 0:
      if i == evenOddPartition:
        evenOddPartition += 1
      else:
        temp = A[i]
        A[i] = A[evenOddPartition]
        A[evenOddPartition] = temp
        evenOddPartition += 1
  return evenOddPartition