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


def find_words(node, word, found_words):
    if (node.index != -1):
        found_words.append(node.index)
    for letter, child in node.children.items():
        find_words(child, word + letter, found_words)


def isValidNode(node, index):
    if node.index == -1:
        return False
    if node.index == index:
        return False
    return True


def addPalindromePairs(words, i, j, pairs):
    pair1 = (i, j)
    if pair1 not in pairs:
        if checkPalindrome(words[i] + words[j]):
            print(f"\"{words[i]}\" and \"{words[j]}\" are palindrome")
            pairs.add(pair1)
    pair2 = (j, i)
    if pair2 not in pairs:
        if checkPalindrome(words[j] + words[i]):
            print(f"\"{words[j]}\" and \"{words[i]}\" are palindrome")
            pairs.add(pair2)


def palindromePairs(words):
    pairs = set()
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
        found = True
        for j in range(len_w - 1, -1, -1):
            if isValidNode(curr_node, i):
                addPalindromePairs(words, i, curr_node.index, pairs)
            inverse += word[j]
            if word[j] in curr_node.children:
                curr_node = curr_node.children[word[j]]
            else:
                found = False
                break
        found_words = []
        if found:
            find_words(curr_node, inverse, found_words)
        # print(f"For {word} found_words = {found_words}")
        for index in found_words:
            if index != i:
                addPalindromePairs(words, i, index, pairs)
    return pairs
            

