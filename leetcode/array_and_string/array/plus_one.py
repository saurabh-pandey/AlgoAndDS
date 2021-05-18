#URL: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
#Description
"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the 
integer.
The digits are stored such that the most significant digit is at the head of the list, and each 
element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
#TODO: Below method uses digit based addition. It would be worthwhile to try converting this list
# to number. Adding one to it and then returning the result as a list back. It would also be good to
# check which method would be faster
def plusOne(digits):
  length = len(digits)
  assert length > 0

  plusOneDigits = []
  carryForward = False
  for i in range(length - 1, -1, -1):
    d = digits[i]
    newD = d
    if i == length - 1:
      newD += 1
    if carryForward:
      newD += 1
    carryForward = False
    if newD == 10:
      carryForward = True
      plusOneDigits.append(0)
    else:
      plusOneDigits.append(newD)
  if carryForward:
    plusOneDigits.append(1)
  
  newLen = len(plusOneDigits)
  for i in range(int(newLen/2)):
    pairId = newLen - 1 - i
    temp = plusOneDigits[i]
    plusOneDigits[i] = plusOneDigits[pairId]
    plusOneDigits[pairId] = temp
  return plusOneDigits




