#URL: https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1053/
#Description
"""
In English, we have a concept called root, which can be followed by some other word to form another 
longer word - let's call this word successor. For example, when the root "an" is followed by the 
successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
replace all the successors in the sentence with the root forming it. If a successor can be replaced 
by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.


Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba 
ababa"
Output: "a a a a a a a a bbb baba a"


Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"


Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Each two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""

class TrieNode:
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
        new_node = TrieNode()
        self.children[c] = new_node
        return new_node


def all_words(trNode, wrd, wrds):
    for c in trNode.children:
        child_node = trNode.children[c]
        if child_node.isAdded:
            wrds.append(wrd + c)
        all_words(child_node, wrd + c, wrds)


def get_prefix_free_trie(dictionary):
    len_sorted_dict = sorted(dictionary, key=len)
    trie_root = TrieNode()
    for w in len_sorted_dict:
        curr_node = trie_root
        for c in w:
            curr_node = curr_node.insert(c)
            if curr_node.isAdded:
                break
        curr_node.isAdded = True
    return trie_root

def replaceWords(dictionary, sentence):
    input_trie = get_prefix_free_trie(dictionary)
    tokens = sentence.split()
    for i in range(len(tokens)):
        word = tokens[i]
        curr_node = input_trie
        replace_with = ""
        for c in word:
            replace_with += c
            if c not in curr_node.children:
                break
            else:
                curr_node = curr_node.children[c]
                if curr_node.isAdded:
                    tokens[i] = replace_with
                    break
    return ' '.join(tokens)
