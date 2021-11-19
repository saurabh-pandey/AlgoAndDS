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
    
    def test_my1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        wordDictionary.addWord("cad")
        assert wordDictionary.search("b") == False
        assert wordDictionary.search("ba") == False
        assert wordDictionary.search("b.") == False
        assert wordDictionary.search("..") == False
        assert wordDictionary.search(".a.") == True
        assert wordDictionary.search("...") == True
        assert wordDictionary.search("....") == False
    
    def test_my2(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("be")
        wordDictionary.addWord("bed")
        wordDictionary.addWord("a")
        wordDictionary.addWord("an")
        wordDictionary.addWord("ant")
        wordDictionary.addWord("ante")
        assert wordDictionary.search("b") == False
        assert wordDictionary.search("be") == True
        assert wordDictionary.search("b.") == True
        assert wordDictionary.search("b..") == True
        assert wordDictionary.search("a") == True
        assert wordDictionary.search("a.") == True
        assert wordDictionary.search("...") == True
        assert wordDictionary.search(".") == True
        assert wordDictionary.search("..") == True
        assert wordDictionary.search("...") == True
        assert wordDictionary.search("....") == True
    
    def test_my3(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("i")
        wordDictionary.addWord("ink")
        assert wordDictionary.search("i") == True
        assert wordDictionary.search("..") == False
        assert wordDictionary.search("i.") == False
        assert wordDictionary.search("i..") == True
        assert wordDictionary.search(".n") == False
        assert wordDictionary.search(".k") == False
        assert wordDictionary.search("...") == True
        assert wordDictionary.search("..k") == True
