#URL: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
#Description
"""
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and 
replace a single character by a different character such that the resulting substring is a 
substring of t. In other words, find the number of substrings in s that differ from some substring 
in t by exactly one character.
For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', 
so this is a valid way.
Return the number of substrings that satisfy the condition above.
A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 
character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.


​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.


Constraints:

1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.
"""
def distance(s, t):
    if len(s) != len(t):
        return -1
    else:
        dist = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                dist += 1
        return dist

# Brute-force
def countSubstring_bf(s, t):
    # print()
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_s = s[i:j]
            # print(f"sub_s = {sub_s}")
            for k in range(len(t)):
                for l in range(k + 1, len(t) + 1):
                    sub_t = t[k:l]
                    # print(f"sub_t = {sub_t}")
                    if distance(sub_s, sub_t) == 1:
                        # print(f"Found {sub_s} <=> {sub_t}")
                        count += 1
    return count


def countSubstring_o3(s, t):
    # print()
    count = 0
    sSz = len(s)
    tSz = len(t)
    maxSz = min(sSz, tSz)
    size = 1
    while size <= maxSz:
        sStart = 0
        sEnd = sStart + size
        while sEnd <= sSz:
            sub_s = s[sStart:sEnd]
            tStart = 0
            tEnd = tStart + size
            while tEnd <= tSz:
                sub_t = t[tStart:tEnd]
                if distance(sub_s, sub_t) == 1:
                    count += 1
                tStart += 1
                tEnd += 1
            sStart += 1
            sEnd += 1
        size += 1            
    return count
