import pytest

import dp.count_sq_matrices as prob

class TestCountSqSubmatrices:
    def test_example1(self):
        matrix = [[0,1,1,1],
                  [1,1,1,1],
                  [0,1,1,1]]
        res = 15
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_example2(self):
        matrix = [[1,0,1],
                  [1,1,0],
                  [1,1,0]]
        res = 7
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_empty1(self):
        matrix = []
        res = 0
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_empty2(self):
        matrix = [[]]
        res = 0
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_one(self):
        matrix = [[1]]
        res = 1
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_zero(self):
        matrix = [[0]]
        res = 0
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_single_row(self):
        matrix = [[1,1,1,0,1]]
        res = 4
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_single_col(self):
        matrix = [[1],
                  [1],
                  [0],
                  [1]]
        res = 3
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_diag(self):
        matrix = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]]
        res = 4
        assert prob.countSquareSubmatrices(matrix) == res
    
    def test_lc1(self):
        matrix = [[0,1,1,1],
                  [1,1,0,1],
                  [1,1,1,1],
                  [1,0,1,0]]
        res = 13
        assert prob.countSquareSubmatrices(matrix) == res
       