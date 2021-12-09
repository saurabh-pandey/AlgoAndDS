import pytest

import trie.palindrome_pairs as prob

class TestPalidromePairs:
    def test_example1(self):
        # words = ["abcd","dcba","lls","s","sssll"]
        # res = [[0,1],[1,0],[3,2],[2,4]]
        # assert prob.palindromePairs(words) == res

        # words = ["a",""]
        # words = ["ab","ba"]
        words = ["ba","abc"]
        # words = ["ab","cba"]
        # words = ["abcd","dcba","lls","s","sssll"]
        print()
        prob.palindromePairs(words)
    
    def test_example2(self):
        words = ["bat","tab","cat"]
        res = [[0,1],[1,0]]
        assert prob.palindromePairs(words) == res
    
    def test_example3(self):
        words = ["a",""]
        res = [[0,1],[1,0]]
        assert prob.palindromePairs(words) == res