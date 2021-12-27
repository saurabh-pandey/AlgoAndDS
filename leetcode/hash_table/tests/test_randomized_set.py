import pytest

from hash_table.randomized_set import RandomizedSet

class TestRandomizedSet:
    def test_example1(self):
        randomizedSet = RandomizedSet()
        assert randomizedSet.insert(1) == True
        assert randomizedSet.remove(2) == False
        assert randomizedSet.insert(2) == True
        assert randomizedSet.getRandom() in [1, 2]
        assert randomizedSet.remove(1) == True
        assert randomizedSet.insert(2) == False
        assert randomizedSet.getRandom() == 2