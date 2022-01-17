import pytest

import dp.count_sq_matrices as prob

class TestCountSqSubmatrices:
    def test_example1(self):
        matrix = [[0,1,1,1],
                  [1,1,1,1],
                  [0,1,1,1]]
        res = 15
        assert prob.countSquareSubmatrices(matrix) == res