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
import operations


def isPalindrome(head):
  # Empty or Single element is considered a palindrome
  if head is None or head._next is None:
    return True
  
  sll_list = operations.toList(head)

  i = 0
  j = len(sll_list) - 1
  while i <= j:
    if sll_list[i] != sll_list[j]:
      return False
    i += 1
    j -= 1
  return True
  # ANOTHER IDEA with O(1) space since above algo is O(n) in space
  # Reverse the second half of the SLL and then compare first with second half