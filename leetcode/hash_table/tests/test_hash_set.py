import pytest

from hash_table.hash_set import MyHashSet


class TestHashSet:
    def test_example1(self):
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        assert myHashSet.contains(1) == True
        assert myHashSet.contains(3) == False
        myHashSet.add(2)
        assert myHashSet.contains(2) == True
        myHashSet.remove(2)
        assert myHashSet.contains(2) == False