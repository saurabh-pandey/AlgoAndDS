import pytest

import trie.replace_words as prob

import pdb

class TestReplaceWords:
    def test_example1(self):
        dictionary = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        res = "the cat was rat by the bat"
        assert prob.replaceWords(dictionary, sentence) == res
    

    def test_example2(self):
        dictionary = ["a","b","c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        res = "a a b c"
        assert prob.replaceWords(dictionary, sentence) == res
    

    def test_example3(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        res = "a a a a a a a a bbb baba a"
        assert prob.replaceWords(dictionary, sentence) == res
    

    def test_example4(self):
        dictionary = ["catt","cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        res = "the cat was rat by the bat"
        assert prob.replaceWords(dictionary, sentence) == res
    

    def test_example5(self):
        dictionary = ["ac","ab"]
        sentence = "it is abnormal that this solution is accepted"
        res = "it is ab that this solution is ac"
        assert prob.replaceWords(dictionary, sentence) == res