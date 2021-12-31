import pytest

import dp.knapsack as prob

import pdb

class TestKnapsack:
    def test_example1(self):
        W = 6
        items = [(3,4), (2,3), (4,2), (4,3)]
        res = [(4,3), (4,2)]
        # pdb.set_trace()
        # prob.solveKnapsack(W, items)
        assert prob.solveKnapsack(W, items) == res