import pytest

import trie.palindrome_pairs as prob

class TestPalidromePairs:
    def test_example1(self):
        words = ["abcd","dcba","lls","s","sssll"]
        res = [[0,1],[1,0],[3,2],[2,4]]
        assert prob.palindromePairs(words) == res
    
    def test_example2(self):
        words = ["bat","tab","cat"]
        res = [[0,1],[1,0]]
        assert prob.palindromePairs(words) == res
    
    def test_example3(self):
        words = ["a",""]
        res = [[0,1],[1,0]]
        assert prob.palindromePairs(words) == res
    
    def test_my1(self):
        words = ["ab","ba"]
        res = [[0,1],[1,0]]
        assert prob.palindromePairs(words) == res
    
    def test_my2(self):
        words = ["ab","ba", "a", "b"]
        res = [[0, 1], [2, 1], [3, 0], [0, 2], [1, 0], [1, 3]]
        assert prob.palindromePairs(words) == res
        # print(prob.palindromePairs(words))
    
    def test_my3(self):
        words = ["ba","abc"]
        res = [[1, 0]]
        assert prob.palindromePairs(words) == res
        # pairs = prob.palindromePairs(words)
        # print(pairs)
    
    def test_my4(self):
        words = ["ab","cba"]
        res = [[0, 1]]
        assert prob.palindromePairs(words) == res
        # pairs = prob.palindromePairs(words)
        # print(pairs)