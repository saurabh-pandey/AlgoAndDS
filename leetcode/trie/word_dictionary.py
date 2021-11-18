#URL: https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1052/
#Description
"""
Design a data structure that supports adding new words and finding if a string matches any 
previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or 
false otherwise. word may contain dots '.' where dots can be matched with any letter. 


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isAdded = False
    
    
    def insert(self, key):
        if key in self.children:
            return self.children[key]
        newNode = TrieNode()
        self.children[key] = newNode
        return newNode
    
    
    def find(self, key):
        if key in self.children:
            return self.children[key]
        return None



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        c_node = self.root
        for w in word:
            c_node = c_node.insert(w)
        c_node.isAdded = True
        

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for w in word:
            if w != ".":
                prev_nodes = nodes[:]
                for node in prev_nodes:
                    if w in node.children:
                        nodes.append(node.children[w])
            else:
                prev_nodes = nodes[:]
                for node in prev_nodes:
                    nodes.extend(node.children.values())
            if not nodes:
                return False
        for node in nodes:
            if node.isAdded:
                return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)