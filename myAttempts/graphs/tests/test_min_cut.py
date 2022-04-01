import pytest

import graphs.min_cut as prob

import os

class TestMinimumCut:
    graph_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "min_cut_graphs")
    
    def test_single(self):
        file_name = "single.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 1
        # assert prob.find_min_cut(file_path) == res
        prob.find_min_cut(file_path)
    
    def test_linear(self):
        file_name = "linear.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 1
        assert prob.find_min_cut(file_path) == res
    
    def test_triangle(self):
        file_name = "triangle.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 2
        assert prob.find_min_cut(file_path) == res
    
    def test_square(self):
        file_name = "square.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 2
        assert prob.find_min_cut(file_path) == res
    
    def test_square_all_diag(self):
        file_name = "square_all_diag.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 3
        assert prob.find_min_cut(file_path) == res
    
    def test_square_diag(self):
        file_name = "square_diag.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 2
        assert prob.find_min_cut(file_path) == res
    
    def test_two_triangles(self):
        file_name = "two_triangles.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 1
        assert prob.find_min_cut(file_path) == res
    
    def test_two_squares(self):
        file_name = "two_squares.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 2
        assert prob.find_min_cut(file_path) == res
    
    def test_double(self):
        file_name = "double.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 2
        assert prob.find_min_cut(file_path) == res
    
    def test_double_single(self):
        file_name = "double_single.txt"
        file_path = os.path.join(TestMinimumCut.graph_dir_path, file_name)
        res = 1
        assert prob.find_min_cut(file_path) == res
