import pytest

from trie.word_dictionary import WordDictionary

class TestWordDictionary:
    def test_example1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") == False
        assert wordDictionary.search("bad") == True
        assert wordDictionary.search(".ad") == True
        assert wordDictionary.search("b..") == True
