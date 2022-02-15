import pytest

import dp.count_teams as prob

class TestCountTeams:
    def test_example1(self):
        rating = [2,5,3,4,1]
        res = 3
        assert prob.numTeams_bf(rating) == res
    
    def test_example2(self):
        rating = [2,1,3]
        res = 0
        assert prob.numTeams_bf(rating) == res
    
    def test_example3(self):
        rating = [1,2,3,4]
        res = 4
        assert prob.numTeams_bf(rating) == res
    