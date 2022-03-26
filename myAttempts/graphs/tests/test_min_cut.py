import pytest

import graphs.min_cut as prob

class TestMinimumCut:
    def test_example1(self):
        file_name = "squares.txt"
        res = 2
        assert prob.find_min_cut(file_name) == res
