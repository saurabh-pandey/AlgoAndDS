#URL: https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
#Description
"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
def lengthOfLongestSubstring_bf(s):
    sz = len(s)
    max_substr_len = 0
    for i in range(sz):
        for j in range(i + 1, sz):
            substr = s[i : j]
            unq_substr = set(substr)
            substr_sz = j - i
            if len(unq_substr) == substr_sz:
                if substr_sz > max_substr_len:
                    max_substr_len = substr_sz
    return max_substr_len


def lengthOfLongestSubstring(s):
    sz = len(s)
    i = 0
    j = 0
    unq_substr = set()
    max_substr_len = 0
    while j < sz:
        if s[j] in unq_substr:
            unq_substr.discard(s[i])
            i += 1
        else:
            unq_substr.add(s[j])
            j += 1
            str_len = len(unq_substr)
            if str_len > max_substr_len:
                max_substr_len = str_len
    
    return max_substr_len
