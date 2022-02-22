import pytest

import dp.stone_game as prob

class TestStoneGame:
    def test_example1(self):
        piles = [5,3,4,5]
        res = True
        # prob.stoneGame_dp(piles)
        prob.stoneGame_dp([3,7,2,3])
        assert prob.stoneGame(piles) == res
    
    def test_example2(self):
        piles = [3,7,2,3]
        res = True
        assert prob.stoneGame(piles) == res
    
    def test_my1(self):
        piles = [4,7,2,3]
        res = True
        assert prob.stoneGame(piles) == res