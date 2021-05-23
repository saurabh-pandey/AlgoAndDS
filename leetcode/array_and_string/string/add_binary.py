#URL: https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
#Description:
"""
Given two binary strings a and b, return their sum as a binary string.


Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
# import pdb

def addBinary(a, b):
  # pdb.set_trace()
  aLen = len(a)
  bLen = len(b)
  if aLen == 0 and bLen == 0:
    return ""
  elif aLen == 0:
    return b
  elif bLen == 0:
    return a
  else:
    binarySum = ""
    # Non zero length string
    biggerStr = ""
    smallerStr = ""
    bigLen = 0
    smallLen = 0
    if aLen >= bLen:
      biggerStr = a
      bigLen = aLen
      smallerStr = b
      smallLen = bLen
    else:
      biggerStr = b
      bigLen = bLen
      smallerStr = a
      smallLen = aLen

    i = bigLen - 1
    j = smallLen - 1
    carryForward = False
    while i >= 0 and j >= 0:
      sum = ""
      bin1 = biggerStr[i]
      bin2 = smallerStr[j]
      if bin1 == "1" and bin2 == "1":
        if carryForward:
          sum = "1"
        else:
          sum = "0"
        carryForward = True
      elif (bin1 == "0" and bin2 == "1") or (bin1 == "1" and bin2 == "0"):
        if carryForward:
          sum = "0"
          carryForward = True
        else:
          sum = "1"
          carryForward = False
      elif bin1 == "0" and bin2 == "0":
        if carryForward:
          sum = "1"
        else:
          sum = "0"
        carryForward = False
      else:
        print(f'Unknown case {bin1}, {bin2}')
      binarySum = sum + binarySum
      i -= 1
      j -= 1
    while i >= 0:
      sum = ""
      bin1 = biggerStr[i]
      if bin1 == "1":
        if carryForward:
          sum = "0"
          carryForward = True
        else:
          sum = "1"
          carryForward = False
      elif bin1 == "0":
        if carryForward:
          sum = "1"
        else:
          sum = "0"
        carryForward = False
      binarySum = sum + binarySum
      i -= 1
    
    if carryForward:
      binarySum = "1" + binarySum
    
    return binarySum

    

        

