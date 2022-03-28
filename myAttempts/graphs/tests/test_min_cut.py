import pytest

import graphs.min_cut as prob

class TestMinimumCut:
    def test_single(self):
        file_name = "single.txt"
        res = 1
        assert prob.find_min_cut(file_name) == res
    
    def test_linear(self):
        file_name = "linear.txt"
        res = 1
        assert prob.find_min_cut(file_name) == res
    
    def test_triangle(self):
        file_name = "triangle.txt"
        res = 2
        assert prob.find_min_cut(file_name) == res
    
    def test_square(self):
        file_name = "square.txt"
        res = 2
        assert prob.find_min_cut(file_name) == res
    
    def test_square_all_diag(self):
        file_name = "square_all_diag.txt"
        res = 3
        assert prob.find_min_cut(file_name) == res
    
    def test_square_diag(self):
        file_name = "square_diag.txt"
        res = 2
        assert prob.find_min_cut(file_name) == res
    
    def test_two_triangles(self):
        file_name = "two_triangles.txt"
        res = 1
        assert prob.find_min_cut(file_name) == res
    
    def test_two_squares(self):
        file_name = "two_squares.txt"
        res = 2
        assert prob.find_min_cut(file_name) == res
