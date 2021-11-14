import pytest

import trie.replace_words as prob

class TestReplaceWords:
    def test_example1(self):
        # dictionary = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        res = "the cat was rat by the bat"

        dictionary = ["aa","a","b"]
        prob.replaceWords(dictionary, sentence)
        # assert prob.replaceWords(dictionary, sentence) == res