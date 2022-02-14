import pytest

import dp.count_teams as prob

class TestCountTeams:
    def test_example1(self):
        rating = [2,5,3,4,1]
        res = 3
        assert prob.numTeams(rating) == res