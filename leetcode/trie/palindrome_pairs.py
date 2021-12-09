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
import pdb


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


def palindromePairs_bf(words):
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


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.index = -1
    
    def insert(self, char):
        if char in self.children:
            return self.children[char]
        else:
            new_node = TrieNode()
            self.children[char] = new_node
            return new_node



def palindromePairs(words):
    pairs = []
    l = len(words)
    if l < 2:
        return pairs
    
    root = TrieNode()
    for i in range(l):
        word = words[i]
        curr_node = root
        for letter in word:
            curr_node = curr_node.insert(letter)
        curr_node.index = i
    
    # pdb.set_trace()
    for i in range(l):
        word = words[i]
        len_w = len(word)
        curr_node = root
        inverse = ""
        for j in range(len_w - 1, -1, -1):
            if (curr_node.index != -1) and (curr_node.index != i):
                if checkPalindrome(word + inverse):
                    print(f"\"{word}\" and \"{inverse}\" are palindrome")
            inverse += word[j]
            if word[j] in curr_node.children:
                curr_node = curr_node.children[word[j]]
            else:
                break
        if (curr_node.index != -1) and (curr_node.index != i):
            if checkPalindrome(word + inverse):
                print(f"\"{word}\" and \"{inverse}\" are palindrome")

