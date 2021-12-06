import pytest

import random
import string

import trie.word_search as prob


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
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_lc3(self):
        board = [["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]]
        words = ["abc","abcd"]
        res = ["abc","abcd"]
        assert set(prob.findWords(board, words)) == set(res)
    
    def test_lc4(self):
        m = 10
        n = 10
        board = []
        entry = ["a", "b"]
        suffix = "babababa"
        for i in range(m):
            row = [0 for _ in range(n)]
            for j in range(n):
                index = (i + j + 1) % 2
                row[j] = entry[index]
            board.append(row)
        words = []
        for first_char in string.ascii_lowercase:
            for second_char in string.ascii_lowercase:
                words.append(first_char + second_char + suffix)
        res = ['bababababa']
        assert prob.findWords(board, words) == res
    
    def test_random(self):
        board_char_bounds = (97, 103)
        board_sz = 12
        words_sz = 30000
        word_len = 10
        board = []
        for i in range(board_sz):
            row = []
            for j in range(board_sz):
                row.append(chr(random.randint(board_char_bounds[0], board_char_bounds[1])))
            board.append(row)
        words = []
        for i in range(words_sz):
            word = ""
            for j in range(random.randint(3, word_len)):
                word += chr(random.randint(board_char_bounds[0], board_char_bounds[1]))
            words.append(word)
        prob.findWords(board, words)