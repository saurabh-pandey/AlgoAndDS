import pytest

import arrays.replace_elem_greatest_right as prob

class TestReplaceElemGreatestRight:
    def test_example1(self):
        arr = [17,18,5,4,6,1]
        expected = [18,6,6,6,1,-1]
        assert prob.replaceElements(arr) == expected
    
    def test_example2(self):
        arr = [400]
        expected = [-1]
        assert prob.replaceElements(arr) == expected
    
    def test_empty(self):
        arr = []
        expected = []
        assert prob.replaceElements(arr) == expected
    
    def test_max_last(self):
        arr = [0,1,2,3,4,5,6]
        expected = [6,6,6,6,6,6,-1]
        assert prob.replaceElements(arr) == expected
    
    def test_descending(self):
        arr = [9,8,7,6,5,4,3,2,1]
        expected = [8,7,6,5,4,3,2,1,-1]
        assert prob.replaceElements(arr) == expected