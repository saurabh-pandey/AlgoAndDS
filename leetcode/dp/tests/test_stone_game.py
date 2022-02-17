import pytest

import dp.stone_game as prob

class TestStoneGame:
    def test_example1(self):
        piles = [5,3,4,5]
        res = True
        assert prob.stoneGame(piles) == res