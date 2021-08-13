import pytest

import recursion_2.largest_rectangle as prob

class TestLargestRectangle:
  def test_example1(self):
    heights = [2,1,5,6,2,3]
    res = 10
    assert prob.largestRectangleArea(heights) == res
  
  
  def test_example2(self):
    heights = [2,4]
    res = 4
    assert prob.largestRectangleArea(heights) == res