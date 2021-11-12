import pytest

from trie.map_sum_pairs import MapSum

class TestMapSumPairs:
    def test_example1(self):
        mapSum = MapSum()
        mapSum.insert("apple", 3)  
        assert mapSum.sum("ap") == 3
        mapSum.insert("app", 2)    
        assert mapSum.sum("ap") == 5
