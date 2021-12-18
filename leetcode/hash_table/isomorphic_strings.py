#URL: https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
#Description
"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order 
of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true


Example 2:

Input: s = "foo", t = "bar"
Output: false


Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
def isIsomorphic(s, t):
    sz = len(s)
    assert sz == len(t)
    s_t_map = {}
    t_s_map = {}
    for i in range(sz):
        s_char = s[i]
        t_char = t[i]
        if s_char in s_t_map:
            if s_t_map[s_char] != t_char:
                return False
        else:
            s_t_map[s_char] = t_char
        if t_char in t_s_map:
            if t_s_map[t_char] != s_char:
                return False
        else:
            t_s_map[t_char] = s_char
    return True
            