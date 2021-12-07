#URL: https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1138/
#Description
"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given 
list, so that the concatenation of the two words words[i] + words[j] is a palindrome.


Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]


Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]


Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
def checkPalindrome(word):
    l = len(word)
    if l < 2:
        return True
    i = 0
    j = l - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def palindromePairs(words):
    pairs = []
    l = len(words)
    if l < 2:
        return pairs
    for i in range(l):
        w1 = words[i]
        for j in range(i + 1, l):
            w2 = words[j]
            if checkPalindrome(w1 + w2):
                pairs.append([i, j])
            if checkPalindrome(w2 + w1):
                pairs.append([j, i])
    return pairs

