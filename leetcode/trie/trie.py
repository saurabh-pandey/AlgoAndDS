#URL: https://leetcode.com/explore/learn/card/trie/147/basic-operations/1047/
#Description
"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and 
retrieve keys in a dataset of strings. There are various applications of this data structure, such 
as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted 
before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that 
has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
class TreeNode:
    def __init__(self) -> None:
        self.isAdded = False
        self.children = {}
    

    def find(self, c):
        if c in self.children:
            return self.children[c]
        return None
    

    def insert(self, c):
        if c in self.children:
            return self.children[c]
        new_node = TreeNode()
        self.children[c] = new_node
        return new_node



class Trie:

    def __init__(self):
        self.root = TreeNode()

    
    def insert(self, word: str) -> None:
        curr_node = self.root
        for w in word:
            curr_node = curr_node.insert(w)
        curr_node.isAdded = True
            


    def search(self, word: str) -> bool:
        curr_node = self.root
        for w in word:
            matching_child = curr_node.find(w)
            if not matching_child:
                return False
            curr_node = matching_child
        return curr_node.isAdded

    
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for w in prefix:
            matching_child = curr_node.find(w)
            if not matching_child:
                return False
            curr_node = matching_child
        return True
    