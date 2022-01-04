import pytest

import dp.sequence_alignment as prob

import pdb

class TestSequenceAlignment:
    def test_example1(self):
        X = "CG"
        Y = "CA"
        p_gap = 3
        p_xy = 7
        res = ("CG_", "C_A", 6)
        # pdb.set_trace()
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
        # assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_example2(self):
        X = "CG"
        Y = "CA"
        p_gap = 3
        p_xy = 5
        res = ("CG", "CA", 5)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
        # assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_example3(self):
        X = "AGGGCT"
        Y = "AGGCA"
        p_gap = 3
        p_xy = 2
        res = ("AGGGCT", "A_GGCA", 5)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
        # assert prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy) == res
    
    def test_my1(self):
        X = "A"
        Y = ""
        p_gap = 3
        p_xy = 2
        res = ("A", "_", 3)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
    
    def test_my2(self):
        X = "A"
        Y = "A"
        p_gap = 3
        p_xy = 2
        res = ("A", "A", 0)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
    
    def test_my3(self):
        X = "A"
        Y = "C"
        p_gap = 3
        p_xy = 2
        res = ("A", "C", 2)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
    
    def test_my4(self):
        X = "A"
        Y = "C"
        p_gap = 2
        p_xy = 5
        res = ("A_", "_C", 4)
        prob.getMinPenaltyAlignment(X, Y, p_gap, p_xy)
