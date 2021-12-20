import pytest

import hash_table.group_anagrams as prob

def checkResult(expected, output):
    expected_sz = len(expected)
    output_sz = len(output)
    if expected_sz != output_sz:
        return False
    for i in range(expected_sz):
        expected[i].sort()
        output[i].sort()
    expected.sort(key=lambda k : (len(k), k))
    output.sort(key=lambda k : (len(k), k))
    return expected == output


class TestGroupAnagrams:
    def test_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        res = [["bat"],["nat","tan"],["ate","eat","tea"]]
        assert checkResult(res, prob.groupAnagrams(strs))
    
    def test_example2(self):
        strs = [""]
        res = [[""]]
        assert checkResult(res, prob.groupAnagrams(strs))
    
    def test_example3(self):
        strs = ["a"]
        res = [["a"]]
        assert checkResult(res, prob.groupAnagrams(strs))