#URL: https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
#Description
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from singly_linked_list.node import Node as ListNode

import math

def addTwoNumbers(l1, l2):
  sumList = None
  firstPtr = l1
  secondPtr = l2
  sumPtr = sumList
  isCarryForward = False
  while firstPtr is not None or secondPtr is not None:
    # Get the sum
    sumVal = 0
    if firstPtr is not None:
      sumVal += firstPtr._val
    if secondPtr is not None:
      sumVal += secondPtr._val
    if isCarryForward:
      sumVal += 1
    
    # Count digits to decide what is the partial sum and if any carry forward
    numDigitsLess1 = 0 if (sumVal == 0) else int(math.log10(sumVal))
    if numDigitsLess1 == 1:
      isCarryForward = True
    else:
      isCarryForward = False
    
    digitPartialSum = sumVal - 10 * numDigitsLess1
    
    # Create the node and add to the result list
    sumNode = ListNode(digitPartialSum)
    if sumList is None:
      sumList = sumNode
      sumPtr = sumList
    else:
      sumPtr._next = sumNode
      sumPtr = sumPtr._next
    
    # Move to next
    if firstPtr is not None:
      firstPtr = firstPtr._next
    if secondPtr is not None:
      secondPtr = secondPtr._next
  
  # Once everything is done and we still have a carry forward attach the last summation digit
  if isCarryForward:
    sumNode = ListNode(1)
    if sumList is None:
      sumList = sumNode
      sumPtr = sumList
    else:
      sumPtr._next = sumNode
      sumPtr = sumPtr._next
  
  return sumList