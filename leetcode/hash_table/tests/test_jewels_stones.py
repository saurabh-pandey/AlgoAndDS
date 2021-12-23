import pytest

import hash_table.jewels_stones as prob

class TestJewelsStones:
    def test_example1(self):
        jewels = "aA"
        stones = "aAAbbbb"
        res = 3
        assert prob.numJewelsInStones(jewels, stones) == res
    
    def test_example2(self):
        jewels = "z"
        stones = "ZZ"
        res = 0
        assert prob.numJewelsInStones(jewels, stones) == res