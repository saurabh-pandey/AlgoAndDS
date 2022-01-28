import pytest

import dp.num_good_splits as prob

class TestNumGoodSplits:
    def test_example1(self):
        s = "aacaba"
        res = 2
        assert prob.numSplits(s) == res