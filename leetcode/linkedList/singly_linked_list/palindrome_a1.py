#URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
# Description
"""
Given the head of a singly linked list, return true if it is a palindrome.


Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
import singly_linked_list.operations_a1 as sll
import singly_linked_list.reverse_a1 as sll_util


def isPalindrome_On_space(head):
  # Empty or Single element is considered a palindrome
  if head is None or head._next is None:
    return True
  
  sll_list = sll.toList(head)

  i = 0
  j = len(sll_list) - 1
  while i <= j:
    if sll_list[i] != sll_list[j]:
      return False
    i += 1
    j -= 1
  return True
  

# Reverse the second half of the SLL and then compare first with second half
def isPalindrome_O1_space(head):
  # Empty or Single element is considered a palindrome
  if head is None or head._next is None:
    return True
  
  sllSize = sll.size(head)
  secondHalf = 0
  if sllSize % 2 == 0:
    secondHalf = int(sllSize/2)
  else:
    secondHalf = int(sllSize/2) + 1
  
  print(f'secondHalf = {secondHalf}')

  currNode = head
  depth = 1
  while depth < secondHalf:
    depth += 1
    currNode = currNode._next
    print(f'currNode = {currNode._val}')
  
  secondHalfPt = currNode._next

  print(f'Before reverse secondHalfPt = {secondHalfPt._val}')
  
  secondHalfPt = sll_util.reverseList(secondHalfPt)

  print(f'After reverse secondHalfPt = {secondHalfPt._val}')
  
  diveSize = int(sllSize/2)
  depth = 1
  currNode = head
  while depth <= diveSize:
    depth += 1
    if currNode._val != secondHalfPt._val:
      return False
    currNode = currNode._next
    secondHalfPt = secondHalfPt._next

  return True


def isPalindrome(head):
  # return isPalindrome_On_space(head)
  return isPalindrome_O1_space(head)