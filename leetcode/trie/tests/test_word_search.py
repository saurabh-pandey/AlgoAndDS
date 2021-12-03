import pytest

import trie.word_search as prob

import pdb

class TestWordSearch:
    def test_example1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        res = ["eat","oath"]
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_example2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        res = []
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_my1(self):
        board = [["a","b"]]
        words = ["a", "ac"]
        res = ["a"]
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_my2(self):
        board = [["a","b"],["c","d"]]
        words = ["dcab", "dbac"]
        res = ["dcab", "dbac"]
        # pdb.set_trace()
        # print(prob.findWords(board, words))
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_empty(self):
        board = [[]]
        words = ["a", "ac"]
        res = []
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_lc1(self):
        board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
        words = ["oa","oaa"]
        res = ["oa","oaa"]
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_lc2(self):
        board = [["a","a"]]
        words = ["aaa"]
        res = []
        # pdb.set_trace()
        # print(prob.findWords(board, words))
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_lc3(self):
        board = [["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]]
        words = ["abc","abcd"]
        res = ["abc","abcd"]
        # pdb.set_trace()
        # print(prob.findWords(board, words))
        assert set(prob.findWords(board, words)) == set(res)