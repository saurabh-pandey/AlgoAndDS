import pytest

from trie.trie import Trie

class TestTrie:
    def test_example1(self):
        tr = Trie()
        tr.insert("apple")
        assert tr.search("apple") == True
        assert tr.search("app") == False
        assert tr.startsWith("app") == True
        tr.insert("app")
        assert tr.search("app") == True
