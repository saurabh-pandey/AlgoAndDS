import pytest

import trie.word_search as prob

class TestWordSearch:
    def test_example1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        res = ["eat","oath"]
        assert prob.findWords(board, words) == res