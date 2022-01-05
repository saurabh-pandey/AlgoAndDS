import pytest

import dp.sequence_alignment as prob


class TestSequenceAlignment:
    def test_example1(self):
        X = "CG"
        Y = "CA"
        p_gap = 3
        p_xy = 7
        res = (6, "CG_", "C_A")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_example2(self):
        X = "CG"
        Y = "CA"
        p_gap = 3
        p_xy = 5
        res = (5, "CG", "CA")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_example3(self):
        X = "AGGGCT"
        Y = "AGGCA"
        p_gap = 3
        p_xy = 2
        res = (5, "AGGGCT", "A_GGCA")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_my1(self):
        X = "A"
        Y = ""
        p_gap = 3
        p_xy = 2
        res = (3, "A", "_")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_my2(self):
        X = "A"
        Y = "A"
        p_gap = 3
        p_xy = 2
        res = (0, "A", "A")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_my3(self):
        X = "A"
        Y = "C"
        p_gap = 3
        p_xy = 2
        res = (2, "A", "C")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_my4(self):
        X = "A"
        Y = "C"
        p_gap = 2
        p_xy = 5
        res = (4, "A_", "_C")
        assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
