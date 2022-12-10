import pytest

import arrays.max_consecutive_ones as prob

class TestMaxConsecutiveOnes:
    def test_case1(self):
        assert prob.find_max_consecutive_ones([1,1,0,1,1,1]) == 3
    
    def test_case2(self):
        assert prob.find_max_consecutive_ones([0,0,0]) == 0
    
    def test_case3(self):
        assert prob.find_max_consecutive_ones([1,1,1,1]) == 4
    
    def test_empty(self):
        assert prob.find_max_consecutive_ones([]) == 0

    def test_case4(self):
        assert prob.find_max_consecutive_ones([0]) == 0
    
    def test_case5(self):
        assert prob.find_max_consecutive_ones([1]) == 1
    
    def test_case6(self):
        assert prob.find_max_consecutive_ones([0,1]) == 1
