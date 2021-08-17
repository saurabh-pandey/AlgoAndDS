import pytest

import recursion_2.skyline as prob

class TestSkyline:
  def test_example1(self):
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    res = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    assert prob.getSkyline(buildings) == res