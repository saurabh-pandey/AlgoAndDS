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
