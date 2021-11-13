import pytest

from trie.map_sum_pairs import MapSum

import pdb

class TestMapSumPairs:
    def test_example1(self):
        mapSum = MapSum()
        # pdb.set_trace()
        mapSum.insert("apple", 3)  
        assert mapSum.sum("ap") == 3
        mapSum.insert("app", 2)    
        assert mapSum.sum("ap") == 5
    
    def test_my1(self):
        mapSum = MapSum()
        # pdb.set_trace()
        assert mapSum.sum("ba") == 0
        mapSum.insert("bat", 3)  
        assert mapSum.sum("ba") == 3
        mapSum.insert("bad", 2)    
        assert mapSum.sum("ba") == 5
        assert mapSum.sum("ca") == 0
        mapSum.insert("ban", 1)
        assert mapSum.sum("ba") == 6
        mapSum.insert("cat", 5)
        assert mapSum.sum("c") == 5
        assert mapSum.sum("ca") == 5
        assert mapSum.sum("cat") == 5
