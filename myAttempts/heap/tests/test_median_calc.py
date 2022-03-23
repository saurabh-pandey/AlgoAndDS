import pytest

import random

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
    
    def test_random(self):
        # print()
        # arr = [12, 1, 14, 8, 13, 12, 10, 11, 11, 12, 6, 8, 6, 8]
        # print(arr)
        # median_calc = prob.MedianCalculator()
        # for num in arr:
        #     median_calc.add(num)
        # arr.sort()
        # print(arr)
        # print(median_calc.median())
        for sz in range(1, 1000):
            # break
            arr = [random.randint(0, sz) for _ in range(sz)]
            orig_arr = arr[:]
            median_calc = prob.MedianCalculator()
            for num in arr:
                median_calc.add(num)
            arr.sort()
            expected_median = 0
            indx = sz//2
            if sz % 2 == 0:
                expected_median = (arr[indx - 1] + arr[indx])/2
            else:
                expected_median = arr[indx]
            if median_calc.median() != expected_median:
                print()
                print(sz, len(arr))
                print(orig_arr)
                print(arr)
                print(median_calc.median())
                print(expected_median)
            # assert median_calc.median() == expected_median