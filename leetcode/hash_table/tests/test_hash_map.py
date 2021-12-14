import pytest

from hash_table.hash_map import MyHashMap

class TestHashMap:
    def test_example1(self):
        myHashMap = MyHashMap()
        myHashMap.put(1, 1)
        myHashMap.put(2, 2)
        assert myHashMap.get(1) == 1
        assert myHashMap.get(3) == -1
        myHashMap.put(2, 1)
        assert myHashMap.get(2) == 1
        myHashMap.remove(2)
        myHashMap.get(2) == -1
