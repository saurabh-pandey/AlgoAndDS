import pytest

import dp.min_cost_tree_leaf_values as prob


class TestMinCostTreeFromLeafValues:
    def test_example1(self):
        arr = [6,2,4]
        res = 32
        assert prob.mct_from_leaf_values(arr) == res