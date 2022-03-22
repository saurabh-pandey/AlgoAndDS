import pytest

import heap.median_calc as prob

class TestMedianCalculator:
    def test_example1(self):
        median_calc = prob.MedianCalculator()
        median_calc.add(1)
        assert median_calc.median() == 1
        median_calc.add(2)
        assert median_calc.median() == 1.5
        median_calc.add(3)
        assert median_calc.median() == 2
        median_calc.add(4)
        assert median_calc.median() == 2.5
        median_calc.add(5)
        assert median_calc.median() == 3
    
    def test_example2(self):
        median_calc = prob.MedianCalculator()
        median_calc.add(5)
        assert median_calc.median() == 5
        median_calc.add(4)
        assert median_calc.median() == 4.5
        median_calc.add(3)
        assert median_calc.median() == 4
        median_calc.add(2)
        assert median_calc.median() == 3.5
        median_calc.add(1)
        assert median_calc.median() == 3