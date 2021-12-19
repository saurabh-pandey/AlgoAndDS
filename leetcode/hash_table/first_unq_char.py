#URL: https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
#Description
"""
Given a string s, find the first non-repeating character in it and return its index. If it does not 
exist, return -1.


Example 1:

Input: s = "leetcode"
Output: 0


Example 2:

Input: s = "loveleetcode"
Output: 2


Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
def firstUniqChar(s):
    char_counter = {}
    for i in range(len(s)):
        char = s[i]
        if char in char_counter:
            char_counter[char][0] += 1
        else:
            char_counter[char] = [1, i]
    for char in char_counter:
        if char_counter[char][0] == 1:
            return char_counter[char][1]
    return -1