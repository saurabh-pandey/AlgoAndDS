#URL: https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1056/
#Description
"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once in a 
word.


Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = 
["oath","pea","eat","rain"]
Output: ["eat","oath"]


Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.isAdded = False
    
    def insert(self, char):
        if char in self.children:
            return self.children[char]
        new_node = TrieNode()
        self.children[char] = new_node
        return new_node
    

def findWords(board, words):
    # Fill Trie
    trie_root = TrieNode()
    for word in words:
        curr_node = trie_root
        for char in word:
            curr_node = curr_node.insert(char)
        curr_node.isAdded = True
    
    # Now BFS on board
    # Use each cell as the starting point
    # Go only as deep as the longest word
    # Retract early if prefix not found in Trie